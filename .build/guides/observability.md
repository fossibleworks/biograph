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
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - .pre-commit-config.yaml
---

The app has no metrics or tracing stack. It relies on Frappe's built-ins:

- **Error Log doctype.** `frappe.log_error(...)` has about 15 call sites. Pass a traceback or message plus a short human title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(title="Error renaming DocType ...")`. Use it for swallowed exceptions in side effects, patches and setup.
- **File logger.** Use `frappe.logger().info(...)` / `.error(...)` for progress and diagnostics in setup, patches and parsing fallbacks (e.g. `patient_duplicate_check.py`, patient_appointment time parsing).
- **User-visible feedback.** Use `frappe.msgprint(..., alert=True)` for success toasts and `indicator="orange"` for degraded outcomes.
- **Do not use** `print()` or debug statements. The pre-commit `debug-statements` hook blocks `pdb`/`breakpoint`.
