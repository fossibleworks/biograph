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
  - .github/workflows/codeql.yml
---

The app has no metrics or tracing stack. Observability relies on Frappe's built-in facilities:

- **Error Log doctype** through `frappe.log_error(...)`. This is the main pattern for failures that don't block the user (notification sending, calendar events, sample collection status, patch failures). Give it a human-readable **title**, e.g. `"Appointment Confirmation Message Not Sent"`, and the traceback (`frappe.get_traceback()`) or the message.
- **Structured app logs** through `frappe.logger()`, with levels `.info()`, `.debug()` and `.error()`. They are used mainly in setup and patches (e.g. `healthcare/setup/patient_duplicate_check.py` logs start, skip, per-rule debug and completion lines) and occasionally for parse failures in `patient_appointment.py`.
- **User feedback**, not logging: `frappe.msgprint` and `frappe.show_alert`.
- Background jobs (`frappe.enqueue`) and scheduler events show up in Frappe's RQ Job and Scheduled Job Log. No custom instrumentation is added.
- **Don't** use `print()` or leave debugger statements. The pre-commit `debug-statements` hook blocks `pdb`/`breakpoint`.
- CI-side tools: Codecov coverage, CodeQL (python, javascript) and Semgrep security scans.
