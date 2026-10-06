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
---

The project relies on Frappe's built-in facilities. There is no external metrics or tracing stack.

- **Error Log DocType:** `frappe.log_error(...)`, about 15 uses, records caught failures. Pass a traceback or message and a short translated title, for example `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- **App logger:** `frappe.logger()` with `.info` / `.debug` / `.error` for setup routines and patches, for example `healthcare/healthcare/setup/patient_duplicate_check.py` logs progress per rule. Use f-strings with counts and names.
- **User-visible signals:** `frappe.msgprint(..., alert=True)` for success toasts, and `indicator="orange"` for degraded-but-continued paths.
- **Realtime:** `frappe.publish_realtime` is used sparingly (sample collection).
- **Background jobs and scheduler:** monitor them through Frappe's RQ Job and Scheduled Job Log. Failures inside jobs should call `log_error`.
- Do not use `print()`. The `debug-statements` pre-commit hook blocks `pdb` and `breakpoint`.
