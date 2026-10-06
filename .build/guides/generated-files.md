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
  - patient_portal/vite.config.js
  - .pre-commit-config.yaml
  - patient_portal/auto-imports.d.ts
  - .releaserc
  - .github/workflows/generate-pot-file.yml
  - crowdin.yml
  - .github/instructions/build-rules.instructions.md
  - AGENTS.md
---

Do not hand-edit these. Regenerate them, or leave them alone.

- **Built Patient Portal assets:** `healthcare/public/frontend/assets/*` (hashed bundles such as `patient_portal-<hash>.js`, which are committed) and `healthcare/www/patient_portal.html`. The frappe-ui vite plugin writes both from `patient_portal/` (`indexHtmlPath`, `outDir`). Edit `patient_portal/src` and rebuild with `yarn build`.
- **Build output:** `healthcare/public/dist/`, `dist/`, `node_modules/` (including `healthcare/public/node_modules`), `*.egg-info`, `__pycache__/`, `.ruff_cache/`. These are gitignored or excluded from linters.
- **Generated type shims:** `patient_portal/auto-imports.d.ts` and `patient_portal/components.d.ts` (unplugin auto-import output).
- **Translations:** the weekly `generate-pot-file.yml` workflow regenerates `healthcare/locale/main.pot`. Crowdin syncs `healthcare/locale/*.po` through `fix: <lang> translations` PRs.
- **Lockfiles:** `yarn.lock`. Change it only through yarn.
- **Release-managed:** semantic-release rewrites the version string in `healthcare/__init__.py`. Do not bump it by hand.
- **Generated from `.build/RULES.md`:** `.github/instructions/build-rules.instructions.md`, `.claude/rules/build-rules.md`, and the BUILD GUIDES block in `AGENTS.md`. Edit the source file instead.
- **DocType JSON** (`doctype/<x>/<x>.json`) is produced by the Frappe DocType editor, but it is versioned source. Edit it carefully and keep `fields` and `field_order` consistent.
- `healthcare/docs/current` is gitignored.
- `.secrets.baseline` is detect-secrets output. Update it with `detect-secrets scan --baseline`.
