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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - patient_portal/src/socket.js
  - .pre-commit-config.yaml
---

# Observability

The app uses Frappe's built-in facilities. There is no external metrics or tracing stack.

- **Error Log doctype via `frappe.log_error`** (about 15 call sites). This is the main way to report failures in background jobs, notifications, calendar events and patches. Always give a human-readable title, e.g. `title="Failed to mark Collected!"` or `_("Appointment Confirmation Message Not Sent")`. Include `frappe.get_traceback()` when catching an exception.
- **`frappe.logger()`** with `.info`, `.debug` and `.error` is used for setup/install progress and parse warnings, e.g. `healthcare/setup/patient_duplicate_check.py` logs rule counts and progress. Use it for operational messages that are not user errors.
- **Do not use `print()` or the stdlib `logging`** in app code. The `debug-statements` pre-commit hook blocks `pdb`/`breakpoint`.
- **Realtime:** the portal listens for `refetch_resource` on socket.io (`patient_portal/src/socket.js`) to refresh data. Server code emits through Frappe realtime.
- **CI:** test runs write bench logs to `bench_run_logs.txt`, and coverage goes to Codecov on scheduled runs.
