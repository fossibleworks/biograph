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
  - .pre-commit-config.yaml
---

There is no metrics or tracing stack. Observability relies on Frappe's built-in facilities:

- **Error Log DocType:** `frappe.log_error(...)` (15 uses) is the main way to record failures. Use a short, human-readable title, either as the second argument or as `title=`, and pass `frappe.get_traceback()` as the message when you are inside `except`. Examples: "Unavailability Calendar Event Error", "Appointment Confirmation Message Not Sent".
- **Logger:** `frappe.logger().info/error(...)` (9 uses) appears mainly in setup and patch code, e.g. `healthcare/setup/patient_duplicate_check.py`, and in parse warnings.
- **Request logs** (`ABDM Request` DocType) store external API calls for the India ABDM integration.
- **CI-side:** Codecov coverage and CodeQL scans.

Do not use `print()` for diagnostics; the `debug-statements` pre-commit hook blocks leftover debuggers.
