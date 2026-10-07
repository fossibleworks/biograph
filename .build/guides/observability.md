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
  - healthcare/hooks.py
  - patient_portal/src/socket.js
---

Observability here relies on Frappe's built-in facilities. There is no external metrics or tracing SDK.

- **Error Log doctype:** `frappe.log_error(message_or_traceback, title)` is the main persistent signal, with about 15 call sites. Give it a stable, human-readable title such as "Appointment Confirmation Message Not Sent" or "Populate Appointment End Fields Patch". Include the document name in the message.
- **App logger:** `frappe.logger().info/error(...)` writes to bench log files, with about 9 call sites. It is used in setup and patches (`healthcare/healthcare/setup/patient_duplicate_check.py`) and when parsing appointment times.
- **Background work:** `scheduler_events` in `hooks.py` and occasional `frappe.enqueue`. Failures show up in the Scheduled Job Log and Error Log.
- **Realtime:** `frappe.publish_realtime` (1 use). The portal holds a socket.io connection (`patient_portal/src/socket.js`).
- **Analytics surfaces:** dashboard charts, chart sources, number cards and reports under `healthcare/healthcare/`.
- **Avoid** `print()` in server code (about 40 occurrences exist, mostly legacy and debugging). Use `frappe.logger()` or `frappe.log_error` instead.
