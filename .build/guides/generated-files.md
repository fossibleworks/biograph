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
  - patient_portal/.gitignore
  - healthcare/public/frontend/assets/patient_portal-5b0abb31.js
  - patient_portal/vite.config.js
  - patient_portal/auto-imports.d.ts
  - .github/workflows/generate-pot-file.yml
  - crowdin.yml
  - .releaserc
  - .pre-commit-config.yaml
  - healthcare/public/node_modules
---

Do not hand-edit these files. Regenerate them instead.

- **Patient portal build output**:
  - `healthcare/public/frontend/assets/*` (hashed `patient_portal-*.js/.css/.js.map`), `healthcare/public/frontend/index.html`
  - `healthcare/public/patient_portal/assets/` (Vite `outDir`)
  - the injected `healthcare/www/patient_portal.html`

  Regenerate with `yarn build`. `dist/` and `dist-ssr` are gitignored.
- **Auto-generated type shims**: `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts`.
- **Translation template**: `healthcare/locale/main.pot`. The weekly `generate-pot-file.yml` workflow regenerates it, and Crowdin syncs `*.po` files back in (`crowdin.yml`).
- **Lockfiles**: `yarn.lock`. Update it through yarn only.
- **DocType JSON** (`doctype/*/*.json`): normally produced by Frappe's DocType editor in developer mode. Edit it carefully so that the field order and `modified` timestamps stay consistent.
- **Version string** in `healthcare/__init__.py`: semantic-release bumps it (`.releaserc`). Do not bump it by hand.
- **`.secrets.baseline`**: maintained by detect-secrets.
- **`healthcare/public/node_modules`**: a symlink to a local bench path. It is not real source.
- **Ignored paths** (`.gitignore`): `*.pyc`, `__pycache__/`, `*.egg-info`, `dist/`, `node_modules/`, `healthcare/docs/current`. The local `.venv/` is untracked.
