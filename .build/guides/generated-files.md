---
title: Generated and vendored files
category: generated-files
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - .gitignore
  - healthcare/public/frontend/index.html
  - patient_portal/vite.config.js
  - .github/workflows/generate-pot-file.yml
  - healthcare/locale/main.pot
  - .releaserc
  - .pre-commit-config.yaml
  - yarn.lock
---

Do not hand-edit these. Regenerate them with their tool instead.

- **Patient portal build output**: `healthcare/public/frontend/` (hashed `assets/patient_portal-*.js/.css`, `.map`, `index.html`) and the Vite output targets in `patient_portal/vite.config.js` (`healthcare/public/patient_portal/assets`, `healthcare/www/patient_portal.html`). Edit `patient_portal/src` and run `yarn build`.
- **Translations template**: `healthcare/locale/main.pot` is regenerated weekly by `generate-pot-file.yml` (`.github/helper/update_pot_file.sh`).
- **Version string** in `healthcare/__init__.py` is rewritten by semantic-release (`.releaserc`).
- **DocType JSON** (`doctype/*/*.json`) is produced by Frappe's DocType editor and exported on save. Keep edits structurally valid. During upstream syncs, merge `fields`/`field_order` as a union.
- **Auto-generated type blocks** (`# begin: auto-generated types`) in controllers are written by Frappe.
- **Lockfiles**: `yarn.lock`. **Ignored** paths: `dist/`, `node_modules/`, `*.egg-info`, `__pycache__/`, `healthcare/docs/current`.
- `.secrets.baseline` is maintained by detect-secrets.
