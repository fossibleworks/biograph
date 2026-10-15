---
title: Generated & vendored files
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
  - healthcare/locale/main.pot
  - .github/workflows/generate-pot-file.yml
  - crowdin.yml
  - .releaserc
  - patient_portal/components.d.ts
  - .pre-commit-config.yaml
---

# Generated & vendored files

Do **not** hand-edit these. Regenerate them with the tool that produced them.

- **Patient Portal build output**: `healthcare/public/frontend/` (hashed `assets/patient_portal-*.js/.css` + `.map`, `index.html`, `manifest.json`), plus anything Vite writes to `healthcare/public/patient_portal/` and `healthcare/www/patient_portal.html` (`indexHtmlPath`). Rebuild with `yarn build`.
- **Translation template**: `healthcare/locale/main.pot`. A weekly workflow regenerates it (`update_pot_file.sh`), and Crowdin syncs `.po` files back as `fix: <lang> translations` PRs.
- **Version string**: `healthcare/__init__.py` `__version__` is bumped by semantic-release on the version-* branches.
- **Lockfiles**: `yarn.lock` (update via yarn only).
- **Ignored build/cache output**: `dist/`, `node_modules/`, `*.egg-info`, `__pycache__/`, `healthcare/docs/current`, `healthcare/public/dist/` (excluded from linters).
- **Symlink**: `healthcare/public/node_modules` points into a local bench. Never commit changes through it.
- **TS declaration stubs**: `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts` are produced by the frappe-ui/unplugin auto-import tooling.
- **DocType JSON** (`doctype/*/*.json`): Desk's DocType editor generates these in developer mode. Editing them by hand is acceptable but must keep the Frappe schema valid.
- `.secrets.baseline` is maintained by `detect-secrets`.
