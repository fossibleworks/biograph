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
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - patient_portal/src/socket.js
  - .pre-commit-config.yaml
---

The repo has no metrics or tracing stack. Observability relies on Frappe built-ins:

- **`frappe.log_error(message, title)`** (~15 uses) writes to the **Error Log** doctype. It is the standard way to record caught exceptions in background, scheduler or integration code. Pass a descriptive title (e.g. "Appointment Confirmation Message Not Sent") and usually `frappe.get_traceback()` as the message.
- **`frappe.logger()`** (~9 uses) for informational and diagnostic file logging, e.g. `frappe.logger().info("Starting patient duplicate check rules setup")` in setup code.
- **`frappe.publish_realtime`** is used for live UI updates. The portal has a `socket.js` client.
- Do not leave `print` or debugger statements: pre-commit `debug-statements` blocks them.
