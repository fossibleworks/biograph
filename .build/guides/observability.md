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
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - patient_portal/src/socket.js
---

Observability relies entirely on Frappe built-ins. There is no metrics or tracing library.

- **Error Log doctype:** `frappe.log_error(message_or_traceback, title)` (~15 sites) is the main mechanism for recording failures that must not break the user flow: notifications, calendar events and patches. The usual form is `frappe.log_error(frappe.get_traceback(), _("<Human title>"))`.
- **File logger:** `frappe.logger().info/error(...)` is used sparingly (~9 sites), mainly in setup and patches and for parse failures.
- **Realtime:** a single `frappe.publish_realtime` call, and the portal has `socket.js`.
- **CI-side:** Codecov coverage on non-PR runs. CodeQL and Semgrep provide security signals.

New code should follow the same pattern: `frappe.log_error` with a descriptive translated title for recoverable failures, and `frappe.throw` for user-facing errors. Never log PHI (patient data) in titles.
