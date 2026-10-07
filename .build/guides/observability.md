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
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - .pre-commit-config.yaml
---

The app relies on Frappe's built-in facilities. It has no external metrics or tracing library.

- **Error Log doctype:** `frappe.log_error(...)` (15 uses) is the main way failures get recorded. Pass a traceback or message plus a human-readable, translated title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(title="Error renaming DocType …")`.
- **App logger:** `frappe.logger().info/error(...)` is used sparingly (about 9 uses), mostly in setup and patches (`patient_duplicate_check`, `setup_patient_duplicate_check_rules`) and for parse failures.
- **Realtime events:** `frappe.publish_realtime` is used once, in sample collection, to push UI updates.
- Do not use `print()` for diagnostics. The pre-commit `debug-statements` hook blocks leftover debugger calls.
