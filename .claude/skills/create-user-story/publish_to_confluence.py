#!/usr/bin/env python3
"""
Converts a User Stories markdown file to Confluence storage format
and creates or updates a Confluence page via the REST API.

Required environment variables:
  CONFLUENCE_BASE_URL        e.g. https://yourcompany.atlassian.net
  CONFLUENCE_USER_EMAIL      your Atlassian account email
  CONFLUENCE_API_TOKEN       Atlassian API token (not your password)
  CONFLUENCE_SPACE_KEY       the Confluence space key, e.g. PROJ
  CONFLUENCE_PARENT_PAGE_ID  (optional) numeric ID of the parent page

Usage:
  python publish_to_confluence.py <path-to-markdown-file> [page-title]
"""

import os
import re
import sys
import json
import base64
import urllib.request
import urllib.error


# ---------------------------------------------------------------------------
# Markdown → Confluence storage format converter
# ---------------------------------------------------------------------------

def md_to_confluence(md: str) -> str:
    lines = md.splitlines()
    output = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Fenced code block
        if line.strip().startswith("```"):
            lang = line.strip()[3:].strip() or "none"
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            code = "\n".join(code_lines)
            output.append(
                f'<ac:structured-macro ac:name="code">'
                f'<ac:parameter ac:name="language">{lang}</ac:parameter>'
                f'<ac:plain-text-body><![CDATA[{code}]]></ac:plain-text-body>'
                f'</ac:structured-macro>'
            )
            i += 1
            continue

        # Horizontal rule (━━━, ─────, ---, ***)
        if re.match(r'^[━─\-\*]{3,}\s*$', line.strip()):
            output.append('<hr/>')
            i += 1
            continue

        # Table
        if line.strip().startswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            output.append(_convert_table(table_lines))
            continue

        # Unordered list
        if re.match(r'^(\s*)[-*+] ', line):
            list_lines = []
            while i < len(lines) and re.match(r'^(\s*)[-*+] ', lines[i]):
                list_lines.append(lines[i])
                i += 1
            output.append(_convert_list(list_lines, ordered=False))
            continue

        # Ordered list
        if re.match(r'^(\s*)\d+\. ', line):
            list_lines = []
            while i < len(lines) and re.match(r'^(\s*)\d+\. ', lines[i]):
                list_lines.append(lines[i])
                i += 1
            output.append(_convert_list(list_lines, ordered=True))
            continue

        # Headings
        heading = re.match(r'^(#{1,6})\s+(.*)', line)
        if heading:
            level = len(heading.group(1))
            text = _inline(heading.group(2))
            output.append(f'<h{level}>{text}</h{level}>')
            i += 1
            continue

        # Blockquote
        if line.startswith('>'):
            text = _inline(line[1:].strip())
            output.append(f'<blockquote><p>{text}</p></blockquote>')
            i += 1
            continue

        # Empty line → paragraph separator
        if line.strip() == '':
            output.append('')
            i += 1
            continue

        # Plain paragraph / decorated line (ASCII art borders etc.)
        text = _inline(line)
        output.append(f'<p>{text}</p>')
        i += 1

    return '\n'.join(output)


def _inline(text: str) -> str:
    """Convert inline markdown to Confluence storage format."""
    # Escape XML special chars first (except & which may already be entity)
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # Bold+italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Strikethrough
    text = re.sub(r'~~(.*?)~~', r'<del>\1</del>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)

    return text


def _convert_list(lines: list, ordered: bool) -> str:
    tag = 'ol' if ordered else 'ul'
    items = []
    for line in lines:
        content = re.sub(r'^(\s*)[-*+\d.]+\s+', '', line)
        items.append(f'<li>{_inline(content)}</li>')
    return f'<{tag}>{"".join(items)}</{tag}>'


def _convert_table(lines: list) -> str:
    rows = []
    for line in lines:
        # Skip separator rows (|---|---|)
        if re.match(r'^\|[\s\-\|:]+\|$', line.strip()):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        rows.append(cells)

    if not rows:
        return ''

    html = ['<table><tbody>']
    for idx, row in enumerate(rows):
        html.append('<tr>')
        cell_tag = 'th' if idx == 0 else 'td'
        for cell in row:
            html.append(f'<{cell_tag}>{_inline(cell)}</{cell_tag}>')
        html.append('</tr>')
    html.append('</tbody></table>')
    return '\n'.join(html)


# ---------------------------------------------------------------------------
# Credentials loader
# ---------------------------------------------------------------------------

def _find_mcp_json(start: str) -> str | None:
    """Walk up from start directory looking for .mcp.json."""
    current = os.path.abspath(start)
    while True:
        candidate = os.path.join(current, '.mcp.json')
        if os.path.isfile(candidate):
            return candidate
        parent = os.path.dirname(current)
        if parent == current:
            return None
        current = parent


def load_atlassian_credentials() -> dict:
    """
    Load Atlassian credentials from .mcp.json (atlassian-confluence server env),
    falling back to environment variables.
    Returns dict with keys: base_url, email, token.
    """
    creds = {}

    mcp_path = _find_mcp_json(os.getcwd())
    if mcp_path:
        with open(mcp_path, encoding='utf-8') as f:
            mcp = json.load(f)
        env = (
            mcp.get('mcpServers', {})
               .get('atlassian-confluence', {})
               .get('env', {})
        )
        site = env.get('ATLASSIAN_SITE_NAME', '')
        if site:
            creds['base_url'] = f'https://{site}.atlassian.net'
        creds['email'] = env.get('ATLASSIAN_USER_EMAIL', '')
        creds['token'] = env.get('ATLASSIAN_API_TOKEN', '')

    # Environment variables override .mcp.json values
    creds['base_url'] = os.environ.get('CONFLUENCE_BASE_URL', creds.get('base_url', '')).rstrip('/')
    creds['email']    = os.environ.get('CONFLUENCE_USER_EMAIL', creds.get('email', ''))
    creds['token']    = os.environ.get('CONFLUENCE_API_TOKEN', creds.get('token', ''))

    return creds


# ---------------------------------------------------------------------------
# Confluence REST API helpers
# ---------------------------------------------------------------------------

def _auth_header(email: str, token: str) -> str:
    credentials = base64.b64encode(f'{email}:{token}'.encode()).decode()
    return f'Basic {credentials}'


def _request(method: str, url: str, headers: dict, body: dict | None = None):
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode()
        print(f'Confluence API error {exc.code}: {error_body}', file=sys.stderr)
        sys.exit(1)


def find_page(base_url: str, headers: dict, space_key: str, title: str) -> dict | None:
    encoded_title = urllib.parse.quote(title)
    url = (
        f'{base_url}/wiki/rest/api/content'
        f'?spaceKey={space_key}&title={encoded_title}&expand=version'
    )
    result = _request('GET', url, headers)
    results = result.get('results', [])
    return results[0] if results else None


def create_page(base_url: str, headers: dict, space_key: str, title: str,
                body: str, parent_id: str | None) -> dict:
    payload = {
        'type': 'page',
        'title': title,
        'space': {'key': space_key},
        'body': {
            'storage': {
                'value': body,
                'representation': 'storage'
            }
        }
    }
    if parent_id:
        payload['ancestors'] = [{'id': parent_id}]
    url = f'{base_url}/wiki/rest/api/content'
    return _request('POST', url, headers, payload)


def update_page(base_url: str, headers: dict, page_id: str, title: str,
                body: str, current_version: int) -> dict:
    payload = {
        'type': 'page',
        'title': title,
        'version': {'number': current_version + 1},
        'body': {
            'storage': {
                'value': body,
                'representation': 'storage'
            }
        }
    }
    url = f'{base_url}/wiki/rest/api/content/{page_id}'
    return _request('PUT', url, headers, payload)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import urllib.parse  # needed inside find_page

    if len(sys.argv) < 2:
        print('Usage: python publish_to_confluence.py <markdown-file> [page-title]')
        sys.exit(1)

    md_path = sys.argv[1]
    if not os.path.exists(md_path):
        print(f'File not found: {md_path}', file=sys.stderr)
        sys.exit(1)

    with open(md_path, encoding='utf-8') as f:
        md_content = f.read()

    # Page title: from arg, or first H1 in the file, or filename
    if len(sys.argv) >= 3:
        title = sys.argv[2]
    else:
        h1 = re.search(r'^#\s+(.+)', md_content, re.MULTILINE)
        title = h1.group(1).strip() if h1 else os.path.splitext(os.path.basename(md_path))[0]

    # Load credentials from .mcp.json, with env var overrides
    creds     = load_atlassian_credentials()
    base_url  = creds['base_url']
    email     = creds['email']
    token     = creds['token']
    space_key = os.environ.get('CONFLUENCE_SPACE_KEY', '')
    parent_id = os.environ.get('CONFLUENCE_PARENT_PAGE_ID', '') or None

    missing = {k: v for k, v in {
        'ATLASSIAN_SITE_NAME / CONFLUENCE_BASE_URL': base_url,
        'ATLASSIAN_USER_EMAIL / CONFLUENCE_USER_EMAIL': email,
        'ATLASSIAN_API_TOKEN / CONFLUENCE_API_TOKEN': token,
        'CONFLUENCE_SPACE_KEY': space_key,
    }.items() if not v}

    if missing:
        print(f'Missing credentials: {", ".join(missing.keys())}', file=sys.stderr)
        print('Auth is read from .mcp.json (atlassian-confluence server env).', file=sys.stderr)
        print('Only CONFLUENCE_SPACE_KEY must be set as an environment variable.', file=sys.stderr)
        sys.exit(1)

    headers = {
        'Authorization': _auth_header(email, token),
        'Content-Type':  'application/json',
        'Accept':        'application/json',
    }

    print(f'Converting "{md_path}" to Confluence storage format...')
    confluence_body = md_to_confluence(md_content)

    print(f'Checking for existing page "{title}" in space {space_key}...')
    existing = find_page(base_url, headers, space_key, title)

    if existing:
        page_id  = existing['id']
        version  = existing['version']['number']
        print(f'Page exists (id={page_id}, v{version}) — updating...')
        result = update_page(base_url, headers, page_id, title, confluence_body, version)
        page_url = f'{base_url}/wiki/pages/{result["id"]}'
        print(f'Page updated: {page_url}')
    else:
        print(f'Creating new page "{title}"...')
        result = create_page(base_url, headers, space_key, title, confluence_body, parent_id)
        page_url = f'{base_url}/wiki/pages/{result["id"]}'
        print(f'Page created: {page_url}')


if __name__ == '__main__':
    main()
