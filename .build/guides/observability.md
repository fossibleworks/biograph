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
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - patient_portal/src/socket.js
  - .github/workflows/codeql.yml
  - .pre-commit-config.yaml
---

Biograph relies on Frappe's built-in facilities. There is no metrics or tracing library.

- **Error Log doctype**: use `frappe.log_error(message_or_traceback, title)` for failures that should not break the user flow. There are about 15 uses, e.g. "Appointment Confirmation Message Not Sent", "Unavailability Calendar Event Error", and patch failures. Pass `frappe.get_traceback()` as the message and give a short, translatable title.
- **Logger**: `frappe.logger().info/error(...)` is used in setup code and patches (`healthcare/setup/patient_duplicate_check.py`, patch `setup_patient_duplicate_check_rules`) and occasionally for parse warnings in `patient_appointment.py`.
- **Realtime**: `frappe.publish_realtime` (1 use) and `patient_portal/src/socket.js` for portal updates.
- **Background jobs** run through `frappe.enqueue` and can be seen in the RQ Job / Scheduled Job Log views.
- **CI-side**: Codecov coverage, CodeQL (Python + JS) and Semgrep security/correctness scans.

Do not add `print` statements; the `debug-statements` pre-commit hook rejects them. Do not log PHI (patient identifiers, clinical details) beyond the document name.
