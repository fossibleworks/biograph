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
  - .github/workflows/generate-pot-file.yml
  - crowdin.yml
  - .releaserc
  - .github/instructions/build-rules.instructions.md
  - AGENTS.md
  - patient_portal/components.d.ts
---

Do not hand-edit these files. Regenerate them with the tool named for each.

- **Patient portal build output**: `healthcare/public/frontend/` (hashed `assets/patient_portal-*.js|.css|.map`, `index.html`, `manifest.json`). These files are committed. Regenerate them with `yarn build`, not by hand. `patient_portal/vite.config.js` also points `outDir` at `healthcare/public/patient_portal/assets` and writes `healthcare/www/patient_portal.html`, so check both paths after a build.
- **`dist/`, `node_modules/`, `healthcare/public/node_modules`, `__pycache__/`, `*.egg-info`**: gitignored build artefacts.
- **`healthcare/locale/main.pot`**: regenerated weekly by `generate-pot-file.yml` (`update_pot_file.sh`). Crowdin manages the translated `*.po` files and syncs them through PRs titled `fix: sync translations from crowdin`.
- **`healthcare/__init__.py` version string**: bumped by semantic-release (`.releaserc` prepareCmd) or by explicit `chore: bump version` commits.
- **`patient_portal/auto-imports.d.ts`, `patient_portal/components.d.ts`**: generated type stubs from the frappe-ui/Vite auto-import plugins.
- **Lockfile**: `yarn.lock`. Update it only through yarn.
- **Build-managed files**: `.github/instructions/build-rules.instructions.md`, `.claude/rules/build-rules.md` and the `BEGIN BUILD GUIDES` block in `AGENTS.md` are generated from `.build/RULES.md`. Edit the source file instead.
- **Doctype `*.json`** files are exported by Frappe when a DocType is saved in developer mode. Editing them by hand is acceptable, but keep `fields` and `field_order` consistent.
- `.secrets.baseline`: maintained by `detect-secrets`.
