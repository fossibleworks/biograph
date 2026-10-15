---
title: Generated Files
category: generated-files
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - .gitignore
  - healthcare/public/frontend/assets/patient_portal-5b0abb31.js
  - patient_portal/vite.config.js
  - patient_portal/components.d.ts
  - .github/workflows/generate-pot-file.yml
  - .releaserc
  - .pre-commit-config.yaml
---

# Generated and vendored files

Do not hand-edit these:

- **`healthcare/public/frontend/assets/*`** are hashed Vite bundles of the patient portal (`patient_portal-<hash>.js/.css/.map`), which are committed. Regenerate them with `yarn build`. They are excluded from pre-commit and prettier.
- **`healthcare/www/patient_portal.html`** is the index HTML written by the frappe-ui Vite plugin (`indexHtmlPath`).
- **`healthcare/public/dist/`** and any `dist/` hold build output. Both are gitignored.
- **`patient_portal/auto-imports.d.ts`** and **`patient_portal/components.d.ts`** are auto-generated type shims from the frappe-ui/unplugin tooling.
- **`healthcare/locale/main.pot`** is regenerated weekly by the `generate-pot-file` workflow (`.github/helper/update_pot_file.sh`). The `.po` translations come from Crowdin PRs.
- **`healthcare/__init__.py` `__version__`** is bumped by semantic-release. Do not change it by hand.
- **Lockfiles:** `yarn.lock`. Update it only through yarn.
- **`.secrets.baseline`** is the detect-secrets baseline. Update it only with `detect-secrets scan --baseline`.
- **`node_modules/`**, `healthcare/public/node_modules` (a symlink into the bench), `__pycache__/`, `*.egg-info`, and `healthcare/docs/current` are gitignored or local-only.
- DocType `*.json` files are written by the Frappe DocType editor. Prefer editing them through Desk and exporting, and keep `modified` timestamps consistent.
