---
title: Commands
category: commands
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - package.json
  - patient_portal/package.json
  - .github/workflows/ci.yml
  - .github/helper/install.sh
  - README.md
  - .pre-commit-config.yaml
  - .github/workflows/semantic-commits.yml
---

All server-side commands run inside a **Frappe bench**. There is no standalone `python -m pytest`.

**Install / setup**
```sh
bench get-app https://github.com/Tacten/biograph   # or the fork URL
bench --site <site> install-app healthcare
bench --site <site> migrate                        # applies doctype JSON + patches.txt
```
CI bootstrap is in `.github/helper/install.sh`. It runs `bench init`, then `get-app payments`/`erpnext`/`healthcare`, `bench setup requirements --dev`, and `install-app`.

**Tests**
```sh
bench --site test_site run-parallel-tests --app healthcare   # CI
bench --site <site> run-tests --app healthcare --module healthcare.healthcare.doctype.patient_appointment.test_patient_appointment
```

**Lint / format** (also enforced in CI)
```sh
pip install pre-commit && pre-commit install
npm install            # eslint deps from root package.json
pre-commit run --all-files    # ruff --fix, ruff-format, eslint, prettier, detect-secrets, pip-audit
git clone --depth 1 https://github.com/frappe/semgrep-rules.git .frappe-semgrep-rules
semgrep ci --config ./.frappe-semgrep-rules/rules --config r/python.lang.correctness
```

**Patient portal**
```sh
yarn install            # root postinstall also installs patient_portal
yarn build              # = cd patient_portal && vite build --base=/assets/healthcare/patient_portal/
cd patient_portal && yarn dev
```

**Commit messages** are checked with commitlint (`npx commitlint --from <base> --to <head>`).
