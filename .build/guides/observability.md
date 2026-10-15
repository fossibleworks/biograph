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
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - eslint.config.mjs
  - .pre-commit-config.yaml
---

The project uses only Frappe's built-in facilities. There is no external metrics or tracing stack.

- **Error Log doctype via `frappe.log_error`** is the main mechanism (about 15 call sites). Pass a descriptive, often translated, **title** and either the exception or `frappe.get_traceback()` as the message:
  ```python
  frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))
  frappe.log_error(message=e, title="Can't bill Service Unit occupancy")
  ```
- **`frappe.logger()`** writes structured file logs in setup/install code (`healthcare/healthcare/setup/patient_duplicate_check.py`) and parsing fallbacks. It is used at `info`/`debug`/`error` levels.
- **Integration request records**: the ABDM integration persists requests as the `ABDM Request` doctype. Healthcare Payment Record tracks payments.
- **Realtime**: `frappe.publish_realtime` and socket.io `refetch_resource` keep the portal fresh. These are not used for telemetry.
- **Avoid `print()` and `console.log`** in app code. ESLint warns on `console`, and the pre-commit `debug-statements` hook blocks leftover debuggers. Existing `print` calls are confined to install/migrate/uninstall scripts and a few legacy modules.
