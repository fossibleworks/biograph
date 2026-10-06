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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/hooks.py
  - .pre-commit-config.yaml
---

The app relies on Frappe's built-in observability. There is no external metrics or tracing SDK.

- **Error Log doctype:** use `frappe.log_error(message_or_traceback, title)` for failures that should be visible to admins. This is the dominant pattern, with about 15 call sites. Use a short, human-readable, translatable title (`_("Appointment Confirmation Message Not Sent")`, `"Unavailability Calendar Event Error"`) and include `frappe.get_traceback()` when inside an `except`.
- **Logger:** `frappe.logger().info/error(...)` for setup, patch and diagnostic lines (patient duplicate check setup, appointment time parsing). Use it sparingly.
- **Background jobs:** `frappe.enqueue` jobs surface in RQ Job and Scheduled Job Log in Desk.
- **Domain audit trail:** Patient Medical Record entries are created and updated through the wildcard `doc_events` hooks. Patient-facing history is an audit artifact, not a log.
- Don't use `print()`. The `debug-statements` pre-commit hook blocks debugger imports.
