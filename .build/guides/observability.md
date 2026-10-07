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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - .pre-commit-config.yaml
---

The app has no dedicated metrics or tracing. It relies on Frappe's built-in facilities:

- **`frappe.log_error(...)`** (15 call sites) writes to the **Error Log** doctype. Use it for failures that must not break the transaction, such as notification sending, calendar event creation and patch steps. Give it a clear translated title, for example `_("Appointment Confirmation Message Not Sent")`, and pass `frappe.get_traceback()` as the message.
- **`frappe.logger()`** (9 call sites) writes `.info`/`.error` lines to bench log files. It is used in patches and for parse failures, for example `frappe.logger().error(f"Could not parse appointment time: ...")`.
- Background jobs started with `frappe.enqueue` show up in the RQ job and scheduler logs.
- CI coverage goes to Codecov, and security scanning goes to CodeQL and Semgrep.

Follow the existing pattern: log_error with a title for anything an admin needs to act on, and logger for diagnostics. Do not use `print`; the `debug-statements` pre-commit hook blocks leftover debuggers.
