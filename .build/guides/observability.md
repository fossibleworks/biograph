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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - patient_portal/src/socket.js
  - .pre-commit-config.yaml
---

The app relies on Frappe's built-in facilities. There is no external metrics or tracing stack.

- **Error Log:** `frappe.log_error(message, title)` (15 call sites) writes to the Error Log doctype. Use a short, descriptive title such as "Unavailability Calendar Event Error", and pass `frappe.get_traceback()` when catching exceptions.
- **Logger:** `frappe.logger()` (about 9 uses), mainly in patches for info and error lines.
- **Realtime:** `frappe.publish_realtime` on the server and the socket.io client in `patient_portal/src/socket.js` for live updates.
- **Background jobs and scheduler** are visible through the standard RQ and Scheduled Job Log views.
- **Integration request logging:** the ABDM integration keeps request records in the `ABDM Request` doctype.
- There is no APM or OpenTelemetry instrumentation in the app code. Do not add `print()`; the pre-commit `debug-statements` hook rejects debugger statements.
