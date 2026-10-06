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
  - patient_portal/src/socket.js
---

Biograph has no metrics or tracing layer. Observability relies on Frappe built-ins:

- **`frappe.log_error(message, title)`** writes to the Error Log doctype and is the main convention (about 15 call sites). Pass `frappe.get_traceback()` or a formatted message, and a short human title such as "Appointment Confirmation Message Not Sent", "Unavailability Calendar Event Error" or "Failed to mark Collected!". Use keyword form `frappe.log_error(title=..., message=...)` where it reads more clearly.
- **`frappe.logger()`** (`.info` / `.error`) is used sparingly (about 9 calls) for patch progress and parse failures.
- Use **`frappe.msgprint`** / realtime (`frappe.publish_realtime`, portal `socket.js`) for user-visible progress, not logs.
- Do not use `print()` debugging. Pre-commit's `debug-statements` hook rejects `pdb` / `breakpoint`.
- Background jobs go through Frappe RQ (`frappe.enqueue`), so failures surface in RQ Job and Error Log.
