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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - .pre-commit-config.yaml
---

Biograph has no metrics or tracing layer. It relies on Frappe's built-in facilities:

- **`frappe.log_error(...)`** (about 15 uses) is the main way to record failures. It writes an **Error Log** document in the desk. Use it with `frappe.get_traceback()` and a translated, descriptive title, e.g. `_("Appointment Confirmation Message Not Sent")`, or with `title=` only. Use it for failures that shouldn't block the user's transaction: notifications, calendar events, patches.
- **`frappe.logger()`** (about 9 uses) does informational or diagnostic logging to the site log files (`.info(...)`, `.error(...)`). It appears mainly in setup and patch code (`healthcare/setup/patient_duplicate_check.py`) and parse fallbacks.
- **User-visible feedback** goes through `frappe.msgprint` and `frappe.throw`, not logs.
- Frappe's Scheduled Job Log captures the outcome of scheduled jobs automatically.

Don't add `print()` (pre-commit runs `debug-statements`) or new logging libraries.
