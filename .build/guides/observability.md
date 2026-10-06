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
  - codecov.yml
---

There is no metrics or tracing stack. Observability relies on Frappe built-ins:

- **Error Log doctype:** `frappe.log_error(frappe.get_traceback(), _("Short Title"))` or `frappe.log_error(title=..., message=...)` inside `except` blocks for failures that shouldn't abort the request (appointment confirmation messages, calendar events, patches). There are about 24 `log_error`/`logger` call sites.
- **Logger:** `frappe.logger().info(...)` and `frappe.logger().error(...)` are used occasionally (patches, time parsing in Patient Appointment).
- **User feedback:** `frappe.msgprint` and `frappe.throw` surface issues in the UI.
- **Coverage reporting:** Codecov, on scheduled CI runs only.
- **Convention:** give log entries a short, translatable Title Case title that names the failed action (for example, `Appointment Confirmation Message Not Sent`), with the traceback as the message. Don't add `print` statements; the pre-commit `debug-statements` hook blocks debugger imports.
