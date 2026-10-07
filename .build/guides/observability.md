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
  - .pre-commit-config.yaml
---

The project uses only Frappe's built-in mechanisms. It has no metrics or tracing libraries.

- **Error Log doctype:** `frappe.log_error(message, title)` or `frappe.log_error(frappe.get_traceback(), title)` is the main way failures are recorded (about two dozen call sites). Use a short, descriptive, human-readable title, for example `'Unavailability Calendar Event Error'` or `'Patient Duplicate Check Rules Setup Failed'`.
- **Logger:** `frappe.logger()` with `.info` / `.error` appears occasionally, mainly in patches.
- Do not use `print` or a raw `logging` module. The pre-commit `debug-statements` hook blocks leftover debuggers.
- Scheduled-job failures surface through Frappe's Scheduled Job Log. The portal SPA has no client telemetry.
