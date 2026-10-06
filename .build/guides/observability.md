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
  - patient_portal/src/socket.js
---

The app has no metrics or tracing. Observability relies on Frappe's built-in tools:

- **Error Log DocType** through `frappe.log_error(...)`, about 15 call sites. Use it for caught failures in notifications, calendar sync, patches and background jobs. Pass a short, human-readable title: either `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(title="…")`.
- **`frappe.logger()`** is used for info and error lines in setup and patch code (`patient_duplicate_check.py`, `setup_patient_duplicate_check_rules.py`) and for parse failures in `patient_appointment.py`.
- **Realtime:** `frappe.publish_realtime` is used once. The portal has a `socket.js` client.
- **JS:** a few `console.log` / `console.error` calls exist in desk and portal code. Do not add more in shipped code.
- **CI-side:** Codecov coverage, CodeQL and semgrep.

For new code, use `frappe.log_error` for anything an admin must notice, and `frappe.logger()` for informational traces. Do not use `print`.
