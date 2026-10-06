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
  - .github/workflows/codeql.yml
---

Observability is minimal and relies on Frappe's built-ins. There are no metrics or tracing libraries.

- **Error Log doctype**:
  - `frappe.log_error(...)` (about 15 calls) is the main tool.
  - Pass a traceback and a translatable title, for example `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`, or use `title=` alone.
  - Use it for failed notifications, calendar sync and patch failures, where the error should not block the user.
- **Logger**:
  - `frappe.logger().info/error(...)` appears sparingly (about 9 calls), mostly in setup and patch code, for example `healthcare/healthcare/setup/patient_duplicate_check.py`.
- **Realtime**:
  - A single `frappe.publish_realtime` call; the portal listens over socket.io (`patient_portal/src/socket.js`).
- **Avoid**:
  - `print()` outside scripts and tests. It goes nowhere in production workers.
  - Logging PHI (patient identifiers, clinical details) in error titles.
- **Security scanning as monitoring**: CodeQL runs weekly, Semgrep and pip-audit run on every PR, and dependabot is configured.
