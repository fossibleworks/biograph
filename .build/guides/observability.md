---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/abdm_request/abdm_request.py
  - .pre-commit-config.yaml
---

There is no dedicated metrics or tracing stack. Observability uses Frappe's built-in facilities:

- **Error Log doctype** via `frappe.log_error(...)` (about 15 uses). This is the main convention for unexpected failures.
  - Pass the traceback (`frappe.get_traceback()`) and a short translatable title, for example `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
  - Or use the `title=` keyword.
- **`frappe.logger()`** is used sparingly (about 9 uses) for informational or error lines in patches and parsing code, for example `frappe.logger().error(f"Could not parse appointment time: ...")`.
- **Do not use `print` or debugger statements.** pre-commit's `debug-statements` hook rejects them.
- **Integration request logs.** ABDM calls are persisted as `ABDM Request` documents, which serve as an audit trail of external calls.
- **CI-side code quality signals** come from CodeQL, Semgrep and Codecov coverage.
