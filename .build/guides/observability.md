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
  - .pre-commit-config.yaml
---

There are no metrics or tracing libraries. Observability comes from Frappe's built-in tools:

- **`frappe.log_error(message, title)`** writes to the Error Log doctype and is the main way to record caught exceptions (about 15 call sites). Give it a descriptive title such as "Unavailability Calendar Event Error".
- **`frappe.logger()`** with `.info()` / `.error()` is used sparingly, mostly in setup and patches (e.g. the patient duplicate check setup).
- **User-visible feedback** goes through `frappe.msgprint` / `alert=True`. **Realtime events** use `frappe.publish_realtime` (rare).
- Background jobs and scheduler runs are visible in the RQ Job and Scheduled Job Log doctypes.

Don't add `print()` debugging. The pre-commit `debug-statements` hook blocks pdb and breakpoints.
