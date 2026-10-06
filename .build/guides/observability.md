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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - patient_portal/src/socket.js
  - .pre-commit-config.yaml
  - .github/workflows/codeql.yml
---

The app has no metrics or tracing. It relies on Frappe's built-in mechanisms:

- **`frappe.log_error`** is the main channel (about 15 calls). It writes to the **Error Log** doctype. Convention: pass the traceback or message plus a translated, human-readable title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(error_msg, "Unavailability Calendar Event Error")`. Use it for failures that should not block the user's transaction.
- **`frappe.logger()`** is used sparingly (about 9 calls) for info and error lines in setup and patches, e.g. `frappe.logger().info("Starting patient duplicate check rules setup")`.
- There are no `print()` statements in app code. The `debug-statements` pre-commit hook blocks leftover debuggers.
- Realtime updates to the UI go through `frappe.publish_realtime` (1 call). The portal subscribes through `patient_portal/src/socket.js`.
- Security and quality signals come from CI: CodeQL (python, javascript), Semgrep, detect-secrets, pip-audit, and Codecov.
