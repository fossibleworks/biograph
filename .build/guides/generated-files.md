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
  - .github/workflows/generate-pot-file.yml
  - .releaserc
  - .github/instructions/build-rules.instructions.md
  - AGENTS.md
  - yarn.lock
---

Do not hand-edit these. Regenerate them instead.

- **Portal build output:** `healthcare/public/patient_portal/assets/` (Vite `outDir`, emptied on every build) and `healthcare/www/patient_portal.html` (Vite `indexHtmlPath`). Edit `patient_portal/src` instead.
- `healthcare/public/frontend/assets/` and `healthcare/public/dist/`: built assets. pre-commit excludes them.
- `dist/`, `node_modules/`, `*.egg-info`, `__pycache__/` and `healthcare/docs/current` are gitignored. `healthcare/public/node_modules` is a tracked link.
- **Lockfile:** `yarn.lock`. Update it only by running yarn.
- **Translations:** `healthcare/locale/main.pot` is regenerated weekly by the `generate-pot-file.yml` workflow (`.github/helper/update_pot_file.sh`).
- **Version string:** `healthcare/__init__.py` `__version__` is bumped by semantic-release.
- **Build-managed mirrors:** `AGENTS.md` (the guides block), `.claude/rules/build-rules.md`, `.cursor/rules/*` and `.github/instructions/build-rules.instructions.md` are generated from `.build/RULES.md`. Edit the source.
- **TS shims:** `patient_portal/auto-imports.d.ts` and `components.d.ts` are written by the frappe-ui Vite plugin.
- `.secrets.baseline` is maintained by detect-secrets.
