---
title: Generated & vendored files
category: generated-files
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - patient_portal/vite.config.js
  - healthcare/public/frontend/assets/patient_portal-5b0abb31.js
  - .github/workflows/generate-pot-file.yml
  - healthcare/locale/main.pot
  - .releaserc
  - .gitignore
  - .pre-commit-config.yaml
  - patient_portal/components.d.ts
---

Do not hand-edit the files below. Regenerate them with the tool that owns them.

- **Portal build output:**
  - `healthcare/public/patient_portal/assets/` and `healthcare/www/patient_portal.html` are written by `patient_portal` `vite build`; the frappe-ui plugin `indexHtmlPath` produces the HTML.
  - `healthcare/public/frontend/assets/*` are committed, hash-named bundles (`patient_portal-<hash>.js/.css/.map`) from an older build.
  - `healthcare/public/dist/` is excluded from lint as build output.
- **Frappe-ui auto-generated typings:** `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts`.
- **Translations:** `healthcare/locale/main.pot` is regenerated every week by `.github/workflows/generate-pot-file.yml` (`.github/helper/update_pot_file.sh`).
- **Version string:** `healthcare/__init__.py` `__version__` is bumped by semantic-release (`.releaserc` prepareCmd). Upstream-sync picks also carry version bumps.
- **Lockfile:** `yarn.lock`, managed by Yarn.
- **Secrets baseline:** `.secrets.baseline`, managed by `detect-secrets`.
- **Ignored (`.gitignore`):** `node_modules/`, `dist/`, `*.egg-info`, `__pycache__/`, `healthcare/docs/current`.
- **Local tool caches and state, not product code:** `.ruff_cache/`, `.goals/`, `.tasks/` and `.env`.
- **DocType JSON** (`<doctype>.json`) is usually written by the Frappe desk DocType editor. Hand edits are allowed. When syncing with upstream, merge `fields`/`field_order` as a 3-way union.
