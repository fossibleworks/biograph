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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - .pre-commit-config.yaml
---

There is no metrics or tracing stack. Observability relies on Frappe built-ins:

- `frappe.log_error(message_or_traceback, title)` writes to the **Error Log** doctype. This is the main mechanism (about 15 calls) and is used for failed notifications, calendar events, and patch failures.
- `frappe.logger().info/error(...)` writes to file logs. It is used sparingly (about 9 calls), mostly in patches and parsing fallbacks.
- Use `frappe.get_traceback()` to attach stack traces.
- No `print` debugging. The pre-commit `debug-statements` hook blocks leftover breakpoints.
