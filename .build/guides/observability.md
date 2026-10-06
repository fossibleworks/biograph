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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - .pre-commit-config.yaml
---

There is no dedicated metrics or tracing stack. Observability relies on Frappe's built-in facilities:

- **`frappe.log_error(message_or_traceback, title)`** writes to the Error Log DocType. This is the main convention for failures that must not abort the user's flow, such as calendar-event sync and patch steps. Give it a short, descriptive title, for example "Unavailability Calendar Event Error".
- **`frappe.logger().info/.error(...)`** is used sparingly, mainly in patches.
- **`frappe.get_traceback()`** is attached when logging exceptions.
- Background jobs (`frappe.enqueue`) and scheduler runs are visible through the RQ Job and Scheduled Job Log views in Frappe.
- CI coverage goes to Codecov, and code scanning uses CodeQL and semgrep.

There are only about 24 logging calls in total. Do not add print statements: the pre-commit `debug-statements` hook blocks debugger imports.
