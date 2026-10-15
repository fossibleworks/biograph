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
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/regional/india/abdm/utils.py
  - .pre-commit-config.yaml
---

Biograph relies on **Frappe's built-in facilities**. It has no metrics or tracing libraries.

- **`frappe.log_error(message_or_traceback, title)`** writes to the Error Log doctype. This is the main pattern (about 15 uses).
  - Typical use: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(error_msg, "Unavailability Calendar Event Error")`.
  - Give it a descriptive title so entries are searchable.
- **`frappe.logger().info/error(...)`** writes to file logs (about 9 uses). It is used for setup and seed progress (`setup/patient_duplicate_check.py`) and parse failures.
- **Request/response audit doctypes**: external API calls (ABDM) are persisted as `ABDM Request` documents holding the request payload and URL. Follow this for new outbound integrations.
- **Realtime**: `frappe.publish_realtime` is used sparingly, and the portal has a socket client (`patient_portal/src/socket.js`).
- Do not use `print()`. The `debug-statements` pre-commit hook blocks pdb/breakpoint.
