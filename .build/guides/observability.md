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
  - healthcare/www/patient_portal.py
  - patient_portal/src/socket.js
  - .pre-commit-config.yaml
---

There is no dedicated metrics or tracing stack. The app relies on Frappe primitives:

- **`frappe.log_error(message, title)`** is the main mechanism (Error Log doctype) for caught failures in background or side-effect work: SMS confirmations, calendar events, payment records, sample collection, medication request processing. Give it a descriptive title, e.g. "Unavailability Calendar Event Error", and include `frappe.get_traceback()` when catching broad exceptions.
- **`frappe.logger()`** is used sparingly for setup progress (`.info`/`.debug` in `setup/patient_duplicate_check.py`) and for parse warnings (`.error`).
- **Telemetry:** `frappe.utils.telemetry.capture("active_site", "patient_portal")` is called when a logged-in user opens the portal (`www/patient_portal.py`).
- **Realtime:** the portal opens a Socket.IO connection (`patient_portal/src/socket.js`) for live updates.
- Avoid bare `print()`. Pre-commit's `debug-statements` hook rejects leftover debuggers.
