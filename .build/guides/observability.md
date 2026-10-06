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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
---

There are no metrics or tracing libraries. Observability uses Frappe built-ins:
- **`frappe.log_error(...)`** (about 15 sites) is the main way to record failures. It writes to the Error Log doctype. The usual pattern is `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`, or `frappe.log_error(title="...")` in patches. Give it a short, human-readable title.
- **`frappe.logger()`** with `.info()` / `.error()` is used sparingly, mainly in setup and patches (`setup/patient_duplicate_check.py`) and for parse failures.
- Don't use `print` or the stdlib `logging` module in app code.
- Background jobs (`frappe.enqueue`, scheduler) report through RQ / Scheduled Job Log in Frappe.
