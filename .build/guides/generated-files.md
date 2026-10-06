---
title: Generated files
category: generated-files
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - .gitignore
  - patient_portal/vite.config.js
  - patient_portal/auto-imports.d.ts
  - patient_portal/components.d.ts
  - .github/workflows/generate-pot-file.yml
  - .releaserc
  - .pre-commit-config.yaml
  - AGENTS.md
---

# Generated and vendored files

Do not hand-edit these files. Regenerate them with their tool.

- **Portal build output**: Vite writes it into `healthcare/public/frontend/` (assets, index.html, manifest) and writes the SPA shell to `healthcare/www/patient_portal.html`. Edit the sources in `patient_portal/src` and rebuild.
- **Auto-generated type shims**: `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts` come from the frappe-ui/unplugin vite plugins.
- **`dist/`, `node_modules/`, `healthcare/public/node_modules`, `__pycache__/`, `*.egg-info`, `healthcare/docs/current`**: gitignored build artifacts.
- **Lockfiles**: `yarn.lock`. Update it only through yarn.
- **Translations**: `healthcare/locale/` (the POT file is regenerated weekly by the `generate-pot-file.yml` workflow via `.github/helper/update_pot_file.sh`). Crowdin manages the translated files.
- **`.secrets.baseline`**: the detect-secrets baseline. Update it with `detect-secrets scan --baseline .secrets.baseline`.
- **Version string in `healthcare/__init__.py`**: semantic-release bumps it on stable branches (`.releaserc`). Do not bump it by hand.
- **Doctype JSON** (`doctype/*/*.json`): normally exported by Frappe when a DocType is saved in Desk. Hand edits are allowed, but they must keep `fields` and `field_order` consistent. On upstream merges, take the 3-way union of fields.
- **Tool mirrors**: Build manages `AGENTS.md` (the BUILD GUIDES block), `.claude/rules/build-rules.md`, `.cursor/rules/`, and `.github/instructions/build-rules.instructions.md`. Edit `.build/RULES.md` instead.
- `.ruff_cache/` is local cache.
