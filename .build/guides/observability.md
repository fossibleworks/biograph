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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.json
  - healthcare/hooks.py
---

There is no metrics or tracing stack. Observability relies on Frappe's built-in facilities.

- **Error Log DocType** via `frappe.log_error(message, title)` (about 15 call sites). Use it for caught exceptions in side-effect paths such as notifications, calendar events and billing. Pass `frappe.get_traceback()` as the message when you have an exception.
- **`frappe.logger()`** for operational info and error logs, e.g. `frappe.logger().info("Starting patient duplicate check rules setup")` in `setup/patient_duplicate_check.py` (9 uses).
- **Document version history**: key DocTypes set `"track_changes": 1` in their JSON (e.g. Patient Appointment).
- **Scheduler jobs** are declared in `hooks.py` `scheduler_events` and show up in Frappe's Scheduled Job Log.

Avoid `print()` in new code. There are about 39 legacy `print(` calls, mostly in patches and setup; prefer `frappe.logger()`. In Desk JS, avoid leaving `console.*` calls.
