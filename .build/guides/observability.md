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
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - .pre-commit-config.yaml
---

# Observability

The project has no metrics or tracing stack. It relies on Frappe's built-ins:

- **`frappe.log_error(message, title)`** writes to the Error Log doctype. Use it for caught exceptions in background jobs, notifications, and billing (about 15 call sites). Give it a descriptive title (for example "Can't bill Service Unit occupancy") and include `frappe.get_traceback()` when you have one.
- **`frappe.logger()`** is used for informational or debug progress in setup routines (`setup/patient_duplicate_check.py`) and for parse warnings. Use `.info` for milestones and `.debug` for per-item detail.
- `print()` and `debug-statements` are blocked by the pre-commit hook. Do not leave them in.
- Never log PHI (patient identifiers or clinical data) into error titles.
