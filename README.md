# PBJ AI Marketplace — Community Edition

Repository-ready OpenAI/Codex plugin marketplace for Indonesian public procurement (PBJ).

## Included plugins

1. **Vanguard PBJ Advisor — Community Edition**
2. **Grandmaster E-Purchasing V6 — Community Edition**
3. **Procurement by Design — Community Edition**

## Master Private policy

The original private plugins remain the authoritative **Master Private** versions and are not modified by this repository. Community Edition packages are separate distribution artifacts. Proprietary books, internal working documents, unpublished templates, and other assets whose redistribution status is not explicitly public are intentionally excluded from the public repository.

Community skills preserve the domain logic and operating principles, while private knowledge packs may be attached separately by the owner in non-public deployments.

## OpenAI-compatible repository layout

- Marketplace catalog: `.agents/plugins/marketplace.json`
- Portable manifest per plugin: `plugin.json`
- OpenAI/Codex compatibility manifest: `.codex-plugin/plugin.json`
- Skills: `skills/<skill-name>/SKILL.md`
- Public/source guidance: `references/`

## Install from GitHub / local checkout

After pushing this folder to GitHub, add it as a marketplace source with Codex:

```bash
codex plugin marketplace add OWNER/REPOSITORY
codex plugin marketplace upgrade pbj-ai-marketplace
```

Or add a local checkout:

```bash
codex plugin marketplace add /absolute/path/to/pbj-ai-marketplace
```

For ChatGPT workspace import, use **Workspace settings → Plugins → Add → Import marketplace**, enter the repository URL, and leave Path empty when this marketplace is at repository root.

## Distribution boundary

This Community Edition does **not** automatically publish the three plugins to OpenAI's universal public directory. It is designed for GitHub-backed marketplace import and repository/local marketplace distribution. Universal-directory submission, if desired, is a separate publication/review step.

## Security and governance

- No secrets, API keys, credentials, workspace IDs, signed download URLs, or private plugin IDs are required at runtime.
- No private Master plugin is overwritten.
- Public versions do not contain private books/document packs by default.
- Legal/regulatory answers should verify current official sources before asserting current law.
- The plugins assist analysis; they do not replace authority of PA/KPA/PPK/PP/Pokja/UKPBJ/auditors or other authorized officials.

## Versioning

Community versions track the upstream Master release they were derived from:

- Vanguard PBJ Advisor: upstream `0.7.1`
- Grandmaster E-Purchasing V6: upstream `1.6.0`
- Procurement by Design: upstream `0.3.0`

See `UPSTREAM.md` for provenance.
