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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - .pre-commit-config.yaml
  - patient_portal/src/socket.js
---

There are no metrics or tracing libraries. Observability uses Frappe's built-in tools:

- **`frappe.log_error(...)`** writes to the **Error Log** DocType (about 15 call sites). Use it for failures that are swallowed so the user flow can continue, such as SMS confirmations, calendar events and patch steps. Pass a short translated title, for example `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`, or `frappe.log_error(title=..., message=...)`.
- **`frappe.logger()`** writes to the bench log files (about 9 uses), for example `frappe.logger().info("Starting patient duplicate check rules setup")` and `.error(f"Could not parse appointment time: {appt_time_str}")`. It is used mostly in setup and patch code.
- **Realtime:** `frappe.publish_realtime` (1 use). The portal has a `socket.js` for Socket.IO.
- No `print()` debugging. The pre-commit `debug-statements` hook blocks `pdb`/`breakpoint`.
- CI gathers coverage and sends it to Codecov on scheduled runs. Security scanning uses CodeQL, semgrep and pip-audit.
