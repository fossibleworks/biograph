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
  - .pre-commit-config.yaml
---

# Observability

The app relies on Frappe's built-in facilities. There is no separate metrics or tracing stack.

- **Error Log doctype.** `frappe.log_error(...)` is the main way to record failures, used ~15 times. Two forms are used:
  - `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`, where the title is a short human-readable string.
  - `frappe.log_error(error_msg, "Unavailability Calendar Event Error")`.
  Use it in `except` blocks around non-critical side effects (messaging, calendar, payments).
- **Logger.** `frappe.logger().info/error(...)` writes to the bench logs (~9 uses), e.g. setup progress in `setup/patient_duplicate_check.py` and parse warnings in `patient_appointment.py`.
- **Telemetry.** The portal entry (`www/patient_portal.py`) calls Frappe telemetry `capture("active_site", "patient_portal")`.
- **Audit trail.** The wildcard submit/cancel hooks write Patient Medical Records. Frappe's version tracking on doctypes provides document history.
- Do not use `print()` for diagnostics in app code. The pre-commit `debug-statements` hook blocks leftover debuggers.
