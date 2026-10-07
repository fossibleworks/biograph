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
  - .pre-commit-config.yaml
  - patient_portal/vite.config.js
  - patient_portal/auto-imports.d.ts
  - .github/workflows/generate-pot-file.yml
  - .releaserc
  - yarn.lock
---

Do not hand-edit these paths:

- **Portal build output:** `healthcare/public/patient_portal/assets` (Vite `outDir`, `emptyOutDir: true`) and the generated `healthcare/www/patient_portal.html` (`indexHtmlPath`). Edit `patient_portal/src` and rebuild.
- **Other built assets:** `healthcare/public/dist/`, `healthcare/public/frontend/assets/` and `dist/` (gitignored and excluded from pre-commit).
- **Auto-generated type stubs:** `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts` (produced by the frappe-ui/unplugin tooling).
- **Translations:** `healthcare/locale/main.pot` is regenerated weekly by the `generate-pot-file.yml` workflow through `.github/helper/update_pot_file.sh`. Wrap strings in `_()` / `__()` instead of editing the POT.
- **Version string:** `healthcare/__init__.py` `__version__` is rewritten by semantic-release (`.releaserc` prepareCmd).
- **Lockfiles:** `yarn.lock` is managed by yarn only.
- **Secrets baseline:** `.secrets.baseline` is managed by `detect-secrets`.
- **Ignored:** `node_modules/`, `__pycache__/`, `*.pyc`, `*.egg-info`, `healthcare/docs/current`, `.ruff_cache`.

DocType `.json` files are produced by the Frappe DocType editor but are committed source. Keep them consistent with that editor's output, including `field_order` and `modified`.
