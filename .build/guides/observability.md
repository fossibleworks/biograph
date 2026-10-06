---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - .github/workflows/codeql.yml
  - .pre-commit-config.yaml
---

Observability here relies on Frappe's built-in mechanisms; the repo has no metrics or tracing library.

- **`frappe.log_error(message_or_traceback, title)`** writes to the Error Log doctype. Use it for failed notifications, calendar-event errors and patch failures (15 call sites). Always give a clear title.
- **`frappe.logger()`** with `.info/.debug/.error` is used for setup and patch progress, e.g. in `healthcare/healthcare/setup/patient_duplicate_check.py`.
- CI saves the bench output to `bench_run_logs.txt`. Coverage XML is uploaded to Codecov on non-PR runs.
- CodeQL runs weekly and on PRs to develop. Semgrep and pip-audit run on every PR.

Do not use `print()` for diagnostics: `debug-statements` is enforced by pre-commit.
