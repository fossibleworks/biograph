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

Observability is Frappe-native only. There is no metrics or tracing library.

- `frappe.log_error(message_or_traceback, title)` records a persistent **Error Log** entry. Use it for failed side effects such as notifications, calendar events and patch failures, and give it a short human-readable title (translated with `_()` in some places).
- `frappe.logger().info/error(...)` writes to the site logs. It is used sparingly, in patches and parse failures.
- `frappe.msgprint` gives user-visible feedback. It is not logging.
- Scheduler and background jobs (`frappe.enqueue`) are visible in Frappe's RQ Job and Scheduled Job Log doctypes.

Do not add `print` statements. The `debug-statements` pre-commit hook rejects leftover debugger calls.
