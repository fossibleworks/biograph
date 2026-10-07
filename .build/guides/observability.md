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

Observability uses Frappe's built-in facilities only. There is no metrics or tracing library.

- **Error Log doctype:** `frappe.log_error(...)` (about 15 call sites) is the main way failures are recorded. Use it with a short, human-readable title, and usually pass `frappe.get_traceback()` as the message:
  ```python
  frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))
  frappe.log_error(error_msg, "Unavailability Calendar Event Error")
  ```
- **App logger:** `frappe.logger().info(...)` / `.error(...)` (about 9 sites), mainly in setup routines and patches (`setup/patient_duplicate_check.py`).
- Do not use `print`. The pre-commit `debug-statements` hook also blocks leftover `pdb`/`breakpoint` calls.
- **Realtime:** the portal opens a socket.io connection (`patient_portal/src/socket.js`) for server push.
- **CI-side signals:** Codecov coverage, CodeQL, Semgrep and pip-audit.
