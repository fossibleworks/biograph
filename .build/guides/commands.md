---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - README.md
  - package.json
  - patient_portal/package.json
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - .github/helper/install.sh
  - .github/workflows/semantic-commits.yml
---

**Install (in a bench):**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Lint and format (the same checks CI runs):**
```sh
pip install pre-commit && pre-commit install
npm install   # eslint deps
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
```

**Semgrep (Frappe rules):**
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient portal:**
```sh
yarn install        # postinstall installs patient_portal
yarn build          # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Tests:** these run inside a bench site, for example `bench --site test_site run-tests --app healthcare`. `.github/helper/install.sh` shows how to set up the CI bench.

**Commit-message check:** `npx commitlint --from <base> --to <head>`.

**Ruff on excluded files:** many legacy paths are excluded from pre-commit, so run `ruff check <file>` on them directly.
