# eplan-development — Claude Code Skill

A Claude Code **skill** for developing with EPLAN Electric P8: C# scripting, the EPLAN API (parts database, properties), and Remote Client automation (including headless EPLAN and Cogineer). Distilled from working production code, with the pitfalls that actually bite (command blocking, message loop, dispose discipline, EPLAN 2025 remoting changes).

When installed, Claude automatically loads this knowledge whenever you ask it to write EPLAN scripts, call EPLAN actions, access the parts database, or build apps that drive EPLAN remotely. It also instructs Claude to verify action names and parameters against the [EPLAN P8 docs RAG](../../cloudflare-rag-eplan-p8/) instead of guessing.

## Contents

```
eplan-development/
├── SKILL.md                          # Entry point: dev models, golden rules, RAG usage
└── references/
    ├── script-basics.md              # Script structure, [Start]/[DeclareAction]/events, deployment
    ├── actions-reference.md          # CommandLineInterpreter + verified action catalog
    ├── core-classes.md               # Progress, PathMap, Settings, MultiLangString, ribbon
    ├── api-data-access.md            # Parts DB (MDPartsManagement), properties, multilang parsing
    ├── remoting.md                   # EplanRemoteClient, dynamic ports, headless, Cogineer
    ├── pitfalls.md                   # Blocking issue, threading, dispose, error handling
    └── integration-patterns.md       # HTTP, SignalR, error forwarding, HTML tools
```

## Install

### Personal (available in all your projects)

```bash
git clone https://github.com/covagashi/Eplan_2026_IA_MCP_scripts
# Windows
xcopy /E /I Eplan_2026_IA_MCP_scripts\claude-skills\eplan-development %USERPROFILE%\.claude\skills\eplan-development
# macOS / Linux
cp -r Eplan_2026_IA_MCP_scripts/claude-skills/eplan-development ~/.claude/skills/eplan-development
```

### Per project

Copy the folder to `<your-project>/.claude/skills/eplan-development` instead.

Restart Claude Code (or start a new session). The skill activates automatically on EPLAN-related tasks, or invoke it explicitly with `/eplan-development`.

## Pairs well with

- **[eplan-p8-mcp-server](../../eplan-p8-mcp-server/)** — lets Claude *execute* EPLAN actions live; this skill teaches it to write correct code and avoid the traps.
- **[cloudflare-rag-eplan-p8](../../cloudflare-rag-eplan-p8/)** — semantic search over the EPLAN P8 docs; the skill tells Claude to consult it before guessing action names/parameters (`POST https://rag2026.covaga.xyz/search`).

## Coverage

EPLAN Electric P8 2022–2025. Version-specific notes included (ribbon API since 2022, remoting default-on in 2023 vs "Remote Client Access" + gRPC in 2025, .NET Framework 4.8.1 targeting).
