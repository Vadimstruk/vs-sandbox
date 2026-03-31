# Installation Guide for Easyterms Agents Module

## Module Location

Your module is ready at:

```
docs/bmb-creations/easyterms-agents/
```

## Installation Steps

### Option 1: Install in Current Project

1. **Copy module to BMAD modules location:**

   ```bash
   cp -r docs/bmb-creations/easyterms-agents /path/to/your/project/_bmad/modules/
   ```

2. **Or use BMAD installer:**
   - Run `bmad install` or `bmad modify`
   - Select "Add Custom Module"
   - Point to `docs/bmb-creations/easyterms-agents`

### Option 2: Install in New Project

1. **Copy the module folder** to your new project
2. **Run BMAD installer:**
   ```bash
   bmad install
   ```
3. **When prompted for local custom modules**, select `easyterms-agents`

## Module Structure

```
easyterms-agents/
├── module.yaml                                    # Module configuration
├── README.md                                      # Module documentation
├── INSTALLATION.md                                # This file
├── agents/
│   └── business-analyst/
│       └── business-analyst.agent.yaml           # Sarah's agent definition
└── _memory/
    └── business-analyst-sidecar/
        ├── memories.md                            # Pattern library (starts empty)
        ├── instructions.md                        # Working protocols
        └── README.md                              # Sidecar documentation
```

## Verification

After installation, verify:

1. **Agent file exists:**

   - `_bmad/agents/business-analyst/business-analyst.agent.yaml` (or compiled `.md`)

2. **Sidecar installed:**

   - `_bmad/_memory/business-analyst-sidecar/memories.md`
   - `_bmad/_memory/business-analyst-sidecar/instructions.md`

3. **Test activation:**
   - Try: `@business-analyst` or `@Sarah`
   - Should see menu with [BR], [LB], [RC], [BA], [PK], [PT], [SM] commands

## Troubleshooting

### Agent Not Found

- Verify module was selected during installation
- Check `_bmad/_config/manifest.yaml` includes the agent
- Ensure agent file is in correct location

### Sidecar Not Loading

- Verify `_memory/business-analyst-sidecar/` folder exists
- Check `memories.md` and `instructions.md` are present
- Review critical_actions in agent YAML use correct paths

### Module Not Appearing

- Verify `module.yaml` is in root of module folder
- Check `code: easyterms-agents` matches folder name
- Ensure module was selected during BMAD installation

## Next Steps

1. **Activate Sarah:**

   ```
   @business-analyst
   ```

2. **Try primary command:**

   ```
   [BR] Create Business Requirement
   ```

3. **Explore capabilities:**
   - [RC] Review Context - Analyze platform
   - [BA] Business Rule Audit - Check consistency
   - [PK] Platform Knowledge - Learn about Easyterms

## Support

For BMAD installation issues, see:
https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/modules/bmb-bmad-builder/custom-content-installation.md
