---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - README.md
  - .github/workflows/ci.yml
  - .pre-commit-config.yaml
  - .github/workflows/linters.v2.yml
  - .github/workflows/semantic-commits.yml
  - package.json
  - patient_portal/package.json
---

**Install (bench)**
```sh
bench get-app https://github.com/Tacten/biograph
bench --site <site> install-app healthcare
```

**Server tests** (from `~/frappe-bench`, as CI runs them)
```sh
bench --site test_site run-parallel-tests --app healthcare --total-builds 1 --build-number 1
# single module (standard Frappe):
bench --site test_site run-tests --app healthcare --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```
CI sets up the bench with `.github/helper/install.sh`.

**Lint and format**
```sh
pip install pre-commit && pre-commit install
npm install          # eslint deps
pre-commit run --all-files   # ruff --fix, ruff-format, prettier, eslint, pip-audit, detect-secrets, yaml/json/toml/ast checks
```

**Semgrep** (also run in CI)
```sh
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
pip install semgrep
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Commit message check**
```sh
npx commitlint --from <base> --to <head>
```

**Patient Portal**
```sh
yarn install         # root postinstall also installs patient_portal
yarn build           # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Sanity check that CI also runs**
```sh
python -m compileall -f .
```
CI also greps for leftover `<<<<<<<` merge-conflict markers.
