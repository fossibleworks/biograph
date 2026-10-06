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
  - .pre-commit-config.yaml
---

There is no external metrics or tracing stack. Observability relies on Frappe's built-in tools:
- **`frappe.log_error(...)`** writes to the Error Log doctype. It is the main convention (about 15 calls). Give it a short, human-readable title, either `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(title=..., message=...)`.
- **`frappe.logger()`** has a few uses (about 9) for info and error lines in patches and parsing fallbacks.
- Background jobs show up in RQ Job / Scheduled Job Log through `frappe.enqueue`.
- Do not use `print()` for diagnostics. The pre-commit `debug-statements` hook blocks leftover debuggers.
