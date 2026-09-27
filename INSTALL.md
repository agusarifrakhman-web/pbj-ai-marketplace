# Installation and publication guide

## Local validation

```bash
python scripts/validate_repository.py
```

## Add marketplace with Codex CLI

```bash
codex plugin marketplace add OWNER/REPOSITORY
codex plugin marketplace list
```

Pin a branch/ref if desired:

```bash
codex plugin marketplace add OWNER/REPOSITORY --ref main
```

## Import to a ChatGPT workspace

1. Open **Workspace settings → Plugins**.
2. Select **Add → Import marketplace**.
3. Enter the GitHub repository URL (repository URL only).
4. Leave **Path** empty if `.agents/plugins/marketplace.json` is at repository root.
5. Select the desired branch/tag/commit if needed.
6. Import and review each plugin's installation policy.

## Before making the GitHub repository public

- Confirm every committed reference file has redistribution rights.
- Keep private Master archives and private knowledge packs out of Git.
- Add an explicit repository/content license only when the owner has selected the desired grant of rights.
- Run validation and inspect `git status` before push.
