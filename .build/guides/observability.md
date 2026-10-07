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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - patient_portal/src/socket.js
  - .pre-commit-config.yaml
---

There is no metrics or tracing stack. Observability uses Frappe's built-ins:

- **Error Log doctype:** `frappe.log_error(frappe.get_traceback(), _("Short Title"))` or `frappe.log_error(title=...)` for caught, non-fatal failures (about 15 call sites). Titles are short, human-readable and translated.
- **Logger:** `frappe.logger().info(...)` / `.error(...)` for setup and patch progress and parse failures (about 9 call sites), e.g. the patient duplicate-check setup.
- **Realtime and background:** background jobs go through `frappe.enqueue`, and their failures surface in the RQ job and Error Log.
- **Patient portal:** uses `socket.js` for realtime updates. There is no client telemetry.

Follow these patterns. Do not add `print()` (the pre-commit `debug-statements` hook blocks debugger statements) or third-party telemetry SDKs.
