# business-analyst-sidecar Sidecar

This folder stores persistent memory for the **Business Analyst** Expert agent (Sarah).

## Purpose

Sarah's sidecar maintains:

- Business rule pattern library (memories.md)
- Working protocols and boundaries (instructions.md)
- Past requirements and insights for pattern matching

## Files

- `memories.md`: Business pattern library, past requirements, insights
- `instructions.md`: Operational protocols, boundaries, working patterns
- `README.md`: This file - sidecar documentation

## Runtime Access

After BMAD installation, this folder will be accessible at:
`{project-root}/_bmad/_memory/business-analyst-sidecar/{filename}.md`

## Usage

Sarah loads these files on startup via critical_actions to:

- Access her pattern library for consistency checking
- Reference past requirements for pattern matching
- Maintain working protocols and boundaries
- Build knowledge over time as the platform evolves
