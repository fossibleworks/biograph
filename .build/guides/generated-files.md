---
title: Generated & vendored files
category: generated-files
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/public/frontend/assets/patient_portal-5b0abb31.js
  - patient_portal/vite.config.js
  - patient_portal/components.d.ts
  - .gitignore
  - .github/workflows/generate-pot-file.yml
  - healthcare/locale/main.pot
  - .releaserc
  - .secrets.baseline
  - yarn.lock
---

Never hand-edit these:

- **Built Patient Portal bundle**: `healthcare/public/frontend/assets/patient_portal-<hash>.js|.css|.js.map`, together with `healthcare/public/frontend/index.html`/`manifest.json`. These are committed build output. Regenerate them with `yarn build`.
  - `patient_portal/vite.config.js` sets `outDir` to `healthcare/public/patient_portal/assets` and `indexHtmlPath` to `healthcare/www/patient_portal.html`.
  - Check where the build actually writes before committing rebuilt assets.
- **frappe-ui auto-generated typings**: `patient_portal/components.d.ts`, `patient_portal/auto-imports.d.ts`.
- **Lockfile**: `yarn.lock`. Update it only through yarn.
- **Translation template**: `healthcare/locale/main.pot`. The weekly *Regenerate POT file* workflow regenerates it (`.github/helper/update_pot_file.sh`). Crowdin syncs the `.po` files.
- **Release version**: semantic-release rewrites the version string in `healthcare/__init__.py` on stable branches.
- **Secrets baseline**: `.secrets.baseline` is maintained by `detect-secrets`.
- **DocType JSON** (`doctype/*/*.json`) is written by the Frappe desk's DocType editor. Hand edits are allowed (the upstream-sync ledger does 3-way unions of `fields`/`field_order`), but they must stay valid Frappe schema.
- **Ignored** (`.gitignore`): `dist/`, `node_modules/`, `__pycache__/`, `*.pyc`, `*.egg-info`, `healthcare/docs/current`. Local-only untracked dirs `.goals/`, `.tasks/`, `.env` and `.ruff_cache` should not be committed.
