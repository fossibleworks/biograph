---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - .pre-commit-config.yaml
---

There are no metrics or tracing libraries. The project relies on Frappe's built-in facilities:

- **Error Log doctype:** `frappe.log_error(message_or_traceback, title)` is the main way to record failures (about 15 call sites). Titles are short and human-readable, e.g. "Appointment Confirmation Message Not Sent" or "Unavailability Calendar Event Error". Pass `frappe.get_traceback()` when inside `except`.
- **App logger:** `frappe.logger().info(...)` / `.error(...)` for setup and patch progress (about 9 call sites, e.g. patient duplicate check setup).
- **Realtime:** `frappe.publish_realtime` pushes status to the browser.
- **Audit trail:** Patient Medical Record entries are created and updated through the wildcard submit/cancel hooks, and Frappe's version tracking covers document history.
- Don't add `print()` or `debug` statements. Pre-commit's `debug-statements` hook rejects them.
