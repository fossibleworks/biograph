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
  - patient_portal/components.d.ts
  - .github/workflows/generate-pot-file.yml
  - crowdin.yml
  - .releaserc
  - .pre-commit-config.yaml
---

# Generated and vendored files

Do not hand-edit these. Regenerate them with the tool that owns them.

| Path | Producer |
|---|---|
| `healthcare/public/frontend/assets/*` (hashed `patient_portal-*.js/.css/.map`) | Built portal bundle (committed) |
| `healthcare/public/patient_portal/assets/` | `vite build` output dir (`emptyOutDir: true`) |
| `healthcare/www/patient_portal.html` | Written by frappe-ui vite plugin (`indexHtmlPath`) |
| `patient_portal/auto-imports.d.ts`, `patient_portal/components.d.ts` | frappe-ui/unplugin auto-import typings |
| `healthcare/locale/main.pot` | Regenerated weekly by `generate-pot-file.yml` (`.github/helper/update_pot_file.sh`) |
| `healthcare/locale/*.po` | Crowdin sync PRs (`crowdin.yml`) |
| `yarn.lock` | Yarn |
| `.secrets.baseline` | `detect-secrets` baseline |
| `healthcare/__init__.py` version string | Bumped by semantic-release `prepareCmd` on release branches |
| `healthcare/public/dist/`, `dist/`, `node_modules/`, `*.egg-info`, `__pycache__/`, `.ruff_cache` | Build and cache output (ignored) |
| `healthcare/docs/current` | Ignored |

DocType `*.json` files are written by Frappe's DocType editor (export-from-desk). When editing them by hand, keep the `fields`/`field_order` structure intact and bump `modified`.

Untracked local engine state (`.goals/`, `.tasks/`, `.env`) must not be committed.
