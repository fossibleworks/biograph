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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/hooks.py
---

There are no external metrics or tracing. Observability relies on Frappe's built-in facilities.

- **`frappe.log_error(...)`** writes an Error Log doctype entry and is the main mechanism (about 15 calls). Pass the traceback plus a short translated title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`, or use the keyword form `frappe.log_error(title=...)`.
- **`frappe.logger()`** goes to file logs (about 9 calls). It's used in patches and parsing fallbacks with `.info` and `.error`.
- **User-visible signals:** `frappe.msgprint(..., indicator="orange")` or `alert=True` for non-fatal failures.
- **Audit trail:** Frappe's document versioning, plus the medical-record timeline created on submit (Patient History Settings).
- **Background jobs** (`frappe.enqueue`) surface through the RQ Job / Error Log UI.
- **Avoid** `print()` debugging, which exists in `patient_appointment.py`, in new code.
