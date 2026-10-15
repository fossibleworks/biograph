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
  - healthcare/public/frontend/assets/patient_portal-5b0abb31.js
  - patient_portal/vite.config.js
  - patient_portal/components.d.ts
  - .github/workflows/generate-pot-file.yml
  - .releaserc
  - .pre-commit-config.yaml
  - healthcare/public/node_modules
---

Do not hand-edit these:

- **Built patient portal bundles:** `healthcare/public/frontend/assets/*` (hashed `patient_portal-*.js`, `.css`, `.map`). Regenerate them with `yarn build` from `patient_portal/`. Pre-commit excludes them.
- **Portal HTML entry:** `healthcare/www/patient_portal.html`. The frappe-ui vite plugin (`indexHtmlPath`) writes it.
- **Auto-generated type stubs:** `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts`.
- **Translation template:** `healthcare/locale/main.pot`. A weekly workflow regenerates it, and Crowdin produces the `*.po` files.
- **DocType JSON** (`doctype/*/*.json`, 133 files): the Frappe DocType editor generates and maintains these. Edit them through Desk or keep them consistent with Frappe's format. Controller `# begin: auto-generated types` blocks are also generated.
- **Version string:** semantic-release bumps `__version__` in `healthcare/__init__.py`.
- **Lockfile:** `yarn.lock`.
- **Ignored:** `dist/`, `node_modules/`, `__pycache__/`, `*.egg-info`, `healthcare/docs/current`.
- `healthcare/public/node_modules` is a committed symlink to a local bench path. Treat it as an environment artifact.
- `.secrets.baseline` is detect-secrets state. Update it with the tool, not by hand.
