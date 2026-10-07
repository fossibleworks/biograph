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
  - .releaserc
  - .github/workflows/generate-pot-file.yml
  - crowdin.yml
  - patient_portal/components.d.ts
  - .secrets.baseline
---

Do not hand-edit these files. Regenerate them with their tool.

- **Build output:** `healthcare/public/dist/`, `healthcare/public/frontend/assets/` (Vite portal build, alongside `healthcare/public/frontend/index.html`), and `dist/`. Pre-commit, prettier and eslint all exclude these paths.
- **Dependencies:** `node_modules/` at any level, including `healthcare/public/node_modules`. Gitignored.
- **Lockfile:** `yarn.lock`. Update it only through yarn.
- **Auto-generated TS declarations:** `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts` (Vite auto-import plugins).
- **Translations:** `healthcare/locale/main.pot` is regenerated weekly by `.github/workflows/generate-pot-file.yml` (`.github/helper/update_pot_file.sh`). `*.po` files come from Crowdin PRs (`fix: sync translations from crowdin`).
- **Version string:** semantic-release rewrites the version in `healthcare/__init__.py` (`.releaserc` prepareCmd). Do not bump it by hand. In the fork, the `.releaserc` version is kept during upstream syncs.
- **Secret scanning baseline:** `.secrets.baseline` (detect-secrets). Update it with `detect-secrets scan --baseline .secrets.baseline`, never by hand.
- **Frappe-managed JSON:** `doctype/*/*.json`, `workspace/*.json`, reports and print formats are normally edited through the Frappe desk (developer mode) and exported. Hand edits must keep valid Frappe schema, including `field_order`/`fields` consistency and `modified` timestamps.
- **Local/agent state:** `.env`, `.goals/`, `.tasks/`, `.ruff_cache/`, `__pycache__/`, `*.egg-info`. Never commit these.
