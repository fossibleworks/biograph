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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - .pre-commit-config.yaml
---

The app has no metrics or tracing stack. It relies on Frappe's built-in facilities:

- **Error Log doctype:** `frappe.log_error(...)` (about 15 uses) is the main way to record failures that are caught and not re-raised. Pass a short, human-readable **title**, usually translated with `_()`, and the traceback or details as the message. Examples: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` and `frappe.log_error(error_msg, "Unavailability Calendar Event Error")`.
- **File logger:** `frappe.logger().info(...)` / `.error(...)` (about 9 uses), mostly in setup and patch code, e.g. *"Starting patient duplicate check rules setup"*, *"... already exist, skipping setup"*, or when parsing appointment times fails.
- **Realtime events:** `frappe.publish_realtime` is used for UI updates (e.g. Sample Collection), and the portal subscribes over socket.io. These are UX signals, not telemetry.
- **External:** CodeQL and Semgrep for code scanning, and Codecov for coverage. There's no APM integration in the repo.

Conventions: never log PHI (patient identifiers or clinical data) in error titles. Avoid `print()`; the pre-commit `debug-statements` hook flags debugger leftovers.
