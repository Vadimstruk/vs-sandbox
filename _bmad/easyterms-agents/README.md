# Easyterms Agents Module

Custom BMAD agents for the Easyterms platform development workflow.

## Module Overview

This module provides specialized agents designed for the Easyterms banking/loans platform, focusing on business analysis and requirement management.

## Components

### Agents

#### Business Analyst (Sarah) 📋

Expert agent specializing in creating business-focused requirements without technical contamination.

**Capabilities:**

- Guided business requirement creation (7-step process)
- Lightweight brainstorming for business needs
- Platform context analysis
- Business rule auditing and consistency checking
- Platform knowledge transfer and onboarding
- Pattern recognition and conflict detection

**Commands:**

- **[BR]** Create Business Requirement - Primary capability
- **[LB]** Lightweight Brainstorming
- **[RC]** Review Context
- **[BA]** Business Rule Audit
- **[PK]** Platform Knowledge
- **[PT]** Pattern Tour
- **[SM]** Save Session

## Installation

### For New Projects

1. Run BMAD installer: `bmad install`
2. When prompted for local custom modules, select `easyterms-agents`
3. Follow installation prompts

### For Existing Projects

1. Run: `bmad modify`
2. Select "Add Custom Module"
3. Choose the `easyterms-agents` folder
4. Complete installation

### Workflows

- **create-business-requirement** — 7-step guided process for validated, Jira-ready business requirements
- **lightweight-brainstorming** — Business-focused ideation (15–20 min) ready for requirement creation

## Module Structure

```
easyterms-agents/
├── module.yaml
├── README.md
├── TODO.md
├── docs/
│   ├── getting-started.md
│   ├── agents.md
│   ├── workflows.md
│   └── examples.md
├── agents/
│   ├── business-analyst.spec.md
│   └── business-analyst/
│       └── business-analyst.agent.yaml
├── workflows/
│   ├── create-business-requirement/
│   └── lightweight-brainstorming/
├── _module-installer/
└── _memory/
    └── business-analyst-sidecar/
        ├── memories.md
        ├── instructions.md
        └── README.md
```

## Documentation

For detailed user guides, see the **[docs/](docs/)** folder:

- [Getting Started](docs/getting-started.md)
- [Agents Reference](docs/agents.md)
- [Workflows Reference](docs/workflows.md)
- [Examples](docs/examples.md)

## Usage

After installation, activate Sarah using:

```
@business-analyst
```

Or use the agent command:

```
[BR] Create Business Requirement
```

## Configuration

This module uses core BMAD configuration variables:

- `user_name`
- `communication_language`
- `document_output_language`
- `output_folder`

No additional configuration required.

## Author

Created for Easyterms platform development workflow.
