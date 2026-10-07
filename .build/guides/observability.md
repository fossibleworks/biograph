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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - .pre-commit-config.yaml
---

Observability uses Frappe's built-in facilities only. There are no metrics or tracing libraries.

- **`frappe.log_error`** (about 15 call sites) writes to the Error Log doctype. Use it for failures that should not abort the user's action: notification sends, calendar-event sync, sample collection, and patches. Give it a clear, translated title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(message=e, title="Failed to mark Collected!")`.
- **`frappe.logger()`** writes to file logs at `.info` / `.error`. It is used sparingly, e.g. for unparseable appointment times and patch progress.
- Do not use `print` or debug statements. The pre-commit `debug-statements` hook rejects leftover `pdb`/`breakpoint`.
- CI coverage goes to Codecov. CodeQL and semgrep provide security signals.
