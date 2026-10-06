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
  - .pre-commit-config.yaml
  - .github/workflows/ci.yml
---

The project has no metrics or tracing stack. Observability relies on Frappe's built-in mechanisms:

- **`frappe.log_error(...)`** writes an **Error Log** document that admins can browse in the desk. This is the main way to surface failures that are swallowed (about 15 sites). Pass a meaningful title, often translated: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`, or `frappe.log_error(title="...")`.
- **`frappe.logger()`** writes to the bench log files with `.info`, `.debug` and `.error`. It is used in setup and patch code, for example `setup/patient_duplicate_check.py` logs progress such as "Creating {n} patient duplicate check rules".
- The stdlib `logging` module and `print` are not used in app code. Pre-commit's `debug-statements` hook blocks leftover debuggers.
- **Audit trail:** Frappe document versioning and timeline comments, plus Patient Medical Record entries that feed the Patient History page.
- **CI** uploads coverage to Codecov on scheduled runs. Bench logs (`bench_run_logs.txt`) are captured during CI install.
