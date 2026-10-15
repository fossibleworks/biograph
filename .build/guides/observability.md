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
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - .pre-commit-config.yaml
---

# Observability

There is no metrics or tracing stack. Observability comes from Frappe's built-in facilities:

- **Error Log DocType** via `frappe.log_error(message, title)`. This is the main mechanism (about 15 call sites), used in scheduler, notification and billing paths. Give it a human-readable title (`"Unavailability Calendar Event Error"`, `_("Appointment Confirmation Message Not Sent")`) and pass `frappe.get_traceback()` or the exception as the message.
- **File logger** via `frappe.logger().info/error(...)` for operational traces in setup routines and parsing fallbacks (`setup/patient_duplicate_check.py`, appointment time parsing).
- **Audit trail** relies on Frappe document versioning, comments and timeline. ABDM calls are persisted as `ABDM Request` documents.
- No `print()` debugging. The `debug-statements` pre-commit hook rejects breakpoints and pdb.
