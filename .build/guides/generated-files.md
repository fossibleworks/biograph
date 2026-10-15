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
  - healthcare/public/frontend/assets/patient_portal-5b0abb31.js
  - patient_portal/vite.config.js
  - .github/workflows/generate-pot-file.yml
  - crowdin.yml
  - .releaserc
  - patient_portal/components.d.ts
  - .secrets.baseline
  - AGENTS.md
---

Never hand-edit these files. Regenerate them with the right tool.

- **Patient Portal build output:** `healthcare/public/frontend/assets/*` (hashed `patient_portal-*.js/.css/.js.map`). This is Vite output and is committed. Regenerate it with `yarn build`. Note that `patient_portal/vite.config.js` sets `outDir` to `healthcare/public/patient_portal/assets`, so check where the build actually lands before committing. Pre-commit excludes `healthcare/public/frontend/assets/` and `healthcare/public/dist/`.
- **frappe-ui/unplugin type stubs:** `patient_portal/components.d.ts` and `patient_portal/auto-imports.d.ts`.
- **Translations:** `healthcare/locale/main.pot` is regenerated weekly by the `generate-pot-file.yml` workflow (`.github/helper/update_pot_file.sh`). Crowdin syncs `healthcare/locale/*.po` through `crowdin.yml`.
- **Version:** semantic-release rewrites the version string in `healthcare/__init__.py`.
- **Lockfiles:** `yarn.lock` at the root.
- **Secrets baseline:** `.secrets.baseline` is maintained by `detect-secrets`.
- **DocType JSON** (`healthcare/healthcare/doctype/*/*.json`, plus workspace, report and number-card JSON) is metadata written by Frappe Desk when you save in developer mode. Edit it through Desk where possible and keep the `modified` timestamp bumped so migrate picks up the changes.
- **Ignored:** `dist/`, `node_modules/`, `__pycache__/`, `*.egg-info`, `healthcare/docs/current`.
- **Build tool mirrors:** `.claude/rules/build-rules.md` and `.github/instructions/build-rules.instructions.md` are mirrors of `.build/RULES.md` maintained by Interactor Build. So is the managed block in `AGENTS.md`/`CLAUDE.md`. Edit the source instead.
