---
title: Tech Stack
category: tech-stack
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - pyproject.toml
  - package.json
  - patient_portal/package.json
  - .github/helper/install.sh
  - .github/workflows/ci.yml
---

- **Backend:** Python ≥3.10 (CI runs 3.14), a **Frappe Framework** app that depends on **ERPNext** and **payments**, all on the version-16 line. Packaged with `flit_core` through `pyproject.toml`. Database is MariaDB (CI uses 11.8) plus Redis.
- **Desk UI:** plain JavaScript Frappe form scripts (`<doctype>.js`, `_list.js`, `_tree.js`), bundled through `healthcare/public/js/healthcare.bundle.js`. HTML/Jinja templates handle print formats and widgets.
- **Patient portal:** Vue 3 with `<script setup>`, Vite 4.4.9, Tailwind CSS 3.4.15, and **frappe-ui** (components plus Tailwind preset), with vue-router and feather/lucide icons. Yarn workspaces (`yarn.lock`).
- **Tooling:** ruff (lint and format), ESLint 10 (flat config), Prettier, pre-commit, detect-secrets, pip-audit, Semgrep with Frappe rules, CodeQL, commitlint, semantic-release, Codecov, Crowdin (i18n), and Mergify.
