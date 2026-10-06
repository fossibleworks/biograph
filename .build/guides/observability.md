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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
---

Observability uses Frappe's built-in facilities. No external metrics or tracing is in place.

- **`frappe.log_error(...)`** (about 15 uses) writes to the Error Log doctype. Use it for failures that must not block the user: messaging, calendar events, patches. Pass a short, translated title and the traceback, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- **`frappe.logger().info/error(...)`** (about 9 uses) is used in setup and patch code for progress messages.
- Avoid `print()` in app code. Existing prints are mostly in patches and setup.
- On the client, `frappe.show_alert` and `msgprint` give user feedback.
- In CI, bench output goes to `bench_run_logs.txt`.
