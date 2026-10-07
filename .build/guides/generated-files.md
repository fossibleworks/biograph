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
  - patient_portal/components.d.ts
  - .github/workflows/generate-pot-file.yml
  - .releaserc
  - .secrets.baseline
---

Do not hand-edit these files:

- **Built portal assets**: `healthcare/public/frontend/assets/*` (hashed `patient_portal-*.js|.css|.map`) and `healthcare/public/dist/`. Regenerate them with `yarn build`. They are excluded from pre-commit.
- **Portal HTML shell**: `healthcare/www/patient_portal.html` is written by the frappe-ui Vite plugin (`indexHtmlPath`).
- **Type stubs**: `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts` are produced by unplugin via frappe-ui/vite.
- **Translations template**: `healthcare/locale/main.pot` is regenerated weekly by `generate-pot-file.yml`.
- **Version string**: `healthcare/__init__.py` `__version__` is bumped by semantic-release, using the exec prepareCmd in `.releaserc`.
- **Lockfiles**: `yarn.lock` must only change via yarn.
- **Doctype JSON** (`doctype/*/*.json`): this is Frappe metadata, normally saved from the DocType editor. When editing it by hand, keep `field_order` and `fields` consistent and bump `modified`. Upstream syncs merge `fields` and `field_order` as a union.
- **Secrets baseline**: `.secrets.baseline` is maintained by detect-secrets.
- **Ignored**: `node_modules/`, `dist/`, `__pycache__/`, `*.egg-info`, `healthcare/docs/current`, `.ruff_cache`.
