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
  - healthcare/public/frontend/index.html
  - patient_portal/vite.config.js
  - .github/workflows/generate-pot-file.yml
  - crowdin.yml
  - .releaserc
  - AGENTS.md
  - .pre-commit-config.yaml
---

Do not hand-edit these paths:

- **Portal build output:** `healthcare/public/frontend/` (hashed `assets/patient_portal-*.js`/`.css` and `.map` files, `index.html`, committed) and `healthcare/public/patient_portal/assets` (Vite `outDir`). Regenerate them with `yarn build`. Do not edit them directly. Pre-commit already excludes `healthcare/public/dist/` and `healthcare/public/frontend/assets/`.
- **Translation template:** `healthcare/locale/main.pot` is regenerated weekly by the `generate-pot-file.yml` workflow. `.po` files arrive through Crowdin PRs (`fix: sync translations from crowdin`).
- **Version string:** `healthcare/__init__.py` is bumped by semantic-release (`chore(release): Bumped to Version …`).
- **Lockfiles:** `yarn.lock`. Update it only through yarn.
- **Secrets baseline:** `.secrets.baseline` is maintained by detect-secrets.
- **Ignored:** `*.pyc`, `__pycache__/`, `*.egg-info`, `dist/`, `node_modules/`, `healthcare/docs/current`, and the local caches `.ruff_cache` and `.frappe-semgrep-rules`.
- **Doctype JSON** (`doctype/*/*.json`) is written by Frappe's DocType editor. When you edit it by hand, keep the `fields`/`field_order` consistency. During upstream merges, take a 3-way union, as `wiki/upstream-sync-version-16.md` describes.
- **Build-managed:** `AGENTS.md` (the guides block), `.claude/rules/build-rules.md`, `.cursor/rules/build-rules.mdc` and `.github/instructions/build-rules.instructions.md` are mirrors of `.build/RULES.md`. Edit the source file instead.
