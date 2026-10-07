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
  - .pre-commit-config.yaml
  - patient_portal/vite.config.js
  - .releaserc
  - .github/workflows/generate-pot-file.yml
  - healthcare/locale/main.pot
  - .secrets.baseline
---

Do not hand-edit these. Regenerate them with the owning tool instead.

- **`healthcare/public/frontend/assets/*`**: hashed Vite build output of the Patient Portal (for example `patient_portal-<hash>.js` and `.js.map`). Rebuild from `patient_portal/` with `yarn build`. pre-commit excludes `healthcare/public/frontend/assets/.*`.
- **`healthcare/www/patient_portal.html`**: the portal's index HTML, written by the frappe-ui Vite plugin (`indexHtmlPath`).
- **`healthcare/public/dist/`** and any `dist/`: build output. These are gitignored and excluded from linters.
- **`node_modules/`** (root, `patient_portal/`, `healthcare/public/node_modules`): gitignored.
- **`yarn.lock`**: lockfile. Change it only through yarn.
- **`healthcare/locale/main.pot`**: translation template, regenerated weekly by the `generate-pot-file.yml` workflow via `.github/helper/update_pot_file.sh`.
- **`patient_portal/auto-imports.d.ts`, `patient_portal/components.d.ts`**: generated type stubs from the frappe-ui/Vite plugins.
- **`healthcare/__init__.py` version string**: semantic-release bumps it via `.releaserc` (`chore(release): Bumped to Version ...`). Do not change it by hand.
- **DocType `.json` files** are written by Frappe's DocType editor (in developer mode). Hand edits are allowed when merging, but keep `fields` and `field_order` consistent.
- **`.secrets.baseline`**: managed by detect-secrets.
- `healthcare/docs/current`, `*.egg-info`, `__pycache__/`, `.ruff_cache/`: gitignored or tool caches.
