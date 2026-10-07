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
  - .gitignore
  - .pre-commit-config.yaml
  - patient_portal/components.d.ts
  - .releaserc
  - .github/workflows/generate-pot-file.yml
---

Do not hand-edit these. Regenerate them, or leave them alone:

- **Patient portal build output:** Vite writes to `healthcare/public/patient_portal/assets` and rewrites the shell `healthcare/www/patient_portal.html` (via `indexHtmlPath`). `healthcare/public/frontend/assets` and `healthcare/public/dist` are also excluded from linting as build output. `dist/` is gitignored.
- **Auto-generated typings:** `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts` (written by the unplugin auto-import and components plugins via frappe-ui).
- **Dependencies:** `node_modules/` (gitignored; `healthcare/public/node_modules` too) and `yarn.lock` (change it only through yarn).
- **Translations:** `healthcare/locale/` POT file, regenerated weekly by `generate-pot-file.yml` / `.github/helper/update_pot_file.sh`.
- **Version string:** semantic-release rewrites the version in `healthcare/__init__.py` on release. Do not bump it by hand.
- **Docs:** `healthcare/docs/current` is gitignored.
- **Secrets baseline:** `.secrets.baseline` is maintained by detect-secrets.
- **Doctype JSON** (`doctype/*/*.json`) is normally exported by the Frappe desk. When merging upstream, union `fields`/`field_order` rather than overwriting.
