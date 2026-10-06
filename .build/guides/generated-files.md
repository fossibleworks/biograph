---
title: Generated & Vendored Files
category: generated-files
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - .gitignore
  - patient_portal/vite.config.js
  - .github/workflows/generate-pot-file.yml
  - crowdin.yml
  - .releaserc
  - patient_portal/components.d.ts
---

Do not hand-edit these. Regenerate them with their tool.

- **Built portal assets:** `healthcare/public/frontend/assets/*` (hashed `patient_portal-<hash>.js/.css/.map`) and Vite output under `healthcare/public/patient_portal/assets`. These are produced by `yarn build`. `healthcare/www/patient_portal.html` is written by the frappe-ui Vite plugin (`indexHtmlPath`).
- `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts`: auto-generated type stubs.
- **Translations:** `healthcare/locale/main.pot` is regenerated weekly by `generate-pot-file.yml`. Crowdin writes `*.po` files (PR title `fix: sync translations from crowdin`).
- **Lockfiles:** `yarn.lock`. Change it only through yarn.
- **Release version:** semantic-release rewrites `healthcare/__init__.py` (`__version__`) on stable branches.
- **DocType JSON** (`doctype/<name>/<name>.json`) is normally exported by Frappe's DocType editor. Keep edits consistent with that format (field order, `modified` timestamp).
- **Ignored:** `node_modules/`, `dist/`, `*.pyc`, `__pycache__/`, `*.egg-info`, `healthcare/docs/current`. Also `.ruff_cache` and local `.goals/`, `.tasks/`, `.env`, which are untracked.
- `.secrets.baseline` is maintained by detect-secrets.
