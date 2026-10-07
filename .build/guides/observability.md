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
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - .pre-commit-config.yaml
---

There is no metrics or tracing stack (no Sentry, StatsD, or OpenTelemetry in app code). Observability relies on Frappe built-ins:

- **Error Log doctype:** `frappe.log_error(frappe.get_traceback(), _("<Human title>"))` or `frappe.log_error(title=...)`. This is the primary failure record, with about 15 call sites.
- **Logger:** `frappe.logger().info(...)` / `.error(...)` for setup and patch progress, and occasional parse failures.
- Background jobs run via `frappe.enqueue`, and scheduler jobs via `hooks.py`. They are visible in the RQ Job and Scheduled Job Log doctypes.
- Avoid `print` and debug statements; the pre-commit `debug-statements` hook rejects them.
