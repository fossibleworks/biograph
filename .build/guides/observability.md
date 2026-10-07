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
  - eslint.config.mjs
  - patient_portal/src/socket.js
---

The app uses **Frappe's built-in facilities**. It has no external metrics or tracing stack.

- **`frappe.log_error(message, title)`** is the main way to record unexpected failures. Entries go to the **Error Log** doctype. Give it a descriptive title ("Unavailability Calendar Event Error") and include `frappe.get_traceback()` when catching exceptions. About 24 call sites use `log_error` or `logger`.
- **`frappe.logger()`** with `.info()` / `.error()` is used for progress messages in patches (`setup_patient_duplicate_check_rules.py`).
- **User-visible feedback** uses `frappe.msgprint` / `frappe.throw`, not logging.
- **Realtime updates:** `self.notify_update()` and socket.io (`patient_portal/src/socket.js`) push document changes to clients.
- **Scheduled job health** is visible in Frappe's Scheduled Job Log, because the jobs are registered through `scheduler_events`.
- **Anti-pattern in existing code:** `print(f"DEBUG - ...")` and `print(f"ERROR - ...")` in `patient_appointment.py`. Stdout is not collected in production. Use `frappe.logger()` or `frappe.log_error` instead.
- In JavaScript, ESLint warns on `console.*` (`no-console: warn`).
