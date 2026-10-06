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
  - healthcare/public/js/mark_unavailable.js
  - .pre-commit-config.yaml
---

The project has no metrics or tracing stack. It relies on Frappe's built-in facilities:

- **Error Log doctype:** `frappe.log_error(message_or_traceback, title)` (15 uses) is the main way to record failures. Pass `frappe.get_traceback()` and a short translated title such as `_("Appointment Confirmation Message Not Sent")` or "Unavailability Calendar Event Error".
- **File logger:** `frappe.logger().info(...)` / `.error(...)` is used in setup and patches (`setup/patient_duplicate_check.py`, `patches/v15_0/setup_patient_duplicate_check_rules.py`) and for parse failures in `patient_appointment.py`.
- **Client side:** `console.error` is used sparingly in desk JS for non-fatal problems. User feedback goes through `frappe.show_alert`.
- Do not use `print` or the stdlib `logging` module directly. pre-commit's `debug-statements` hook rejects leftover debuggers.
