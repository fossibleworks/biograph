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
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - patient_portal/src/socket.js
---

There is no metrics or tracing stack. Observability relies on Frappe built-ins:

- **`frappe.log_error(...)`** writes Error Log records, which is the main way to surface failures (about 15 call sites). Pass the traceback and a short, human-readable **title**, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(error_msg, "Unavailability Calendar Event Error")`.
- **`frappe.logger().info/error(...)`** is used sparingly (setup and patch progress, unparsable appointment times). Do not use the stdlib `logging` module or `print`.
- **Background jobs** go through `frappe.enqueue`, so failures appear in RQ Job / Error Log.
- **Realtime:** the portal opens a socket connection (`patient_portal/src/socket.js`). `frappe.publish_realtime` is rarely used.
- **User-facing feedback** uses `frappe.msgprint` / `frappe.throw` on the server and `frappe.show_alert` / `frappe.msgprint` in Desk JS.
- **Never log PHI** (patient names, diagnoses, identifiers) in Error Log titles. Put it in the record link, not the title.
