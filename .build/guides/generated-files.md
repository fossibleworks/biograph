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
  - patient_portal/vite.config.js
  - healthcare/public/frontend/index.html
  - .github/workflows/generate-pot-file.yml
  - crowdin.yml
  - .releaserc
  - .pre-commit-config.yaml
  - AGENTS.md
---

Do not hand-edit these. Regenerate them or leave them alone.

- **`healthcare/public/frontend/`**: committed, hashed Vite build of the patient portal (`assets/patient_portal-<hash>.js/.css/.map`, `index.html`, `manifest.json`).
- **`healthcare/public/patient_portal/assets/`** and **`healthcare/www/patient_portal.html`**: the current Vite `outDir` and `indexHtmlPath` targets, written by `yarn build`.
- **`healthcare/public/dist/`**: Frappe asset build output. It is excluded from pre-commit and semgrep.
- **`healthcare/locale/main.pot`**: regenerated weekly by the `generate-pot-file.yml` workflow (`.github/helper/update_pot_file.sh`). The `.po` translations come from Crowdin (`crowdin.yml`).
- **`healthcare/__init__.py` `__version__`**: bumped by semantic-release (`.releaserc` `prepareCmd`) on version branches only. The fork keeps its own version.
- **Lockfiles:** `yarn.lock`. Change it only through yarn.
- **Ignored artifacts:** `*.pyc`, `__pycache__/`, `*.egg-info`, `dist/`, `node_modules/`, `healthcare/docs/current`, `.ruff_cache`.
- **`.secrets.baseline`**: the detect-secrets baseline. Update it with `detect-secrets scan --baseline .secrets.baseline`, not by hand.
- **DocType `.json` files** are normally saved from the Frappe desk in developer mode. When editing them by hand, keep `fields` and `field_order` consistent.
- **Build-managed:** the guides block in `AGENTS.md`, `.build/`, and the `.claude/rules/build-rules.md` and `.github/instructions/build-rules.instructions.md` mirrors are overwritten by Interactor Build.
