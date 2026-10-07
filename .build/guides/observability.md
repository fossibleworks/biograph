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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/hooks.py
  - .pre-commit-config.yaml
---

Biograph relies on **Frappe's built-in facilities**. There is no separate metrics or tracing stack.

- **Error Log DocType**: `frappe.log_error(...)` records failures that should not interrupt the user, with about 15 call sites.
  - Pass the traceback plus a short translated title: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
  - Or pass a keyword title: `frappe.log_error(title="Error renaming DocType …")`.
- **Logger**: `frappe.logger().info/error(...)` is used sparingly, about 9 calls, for setup and patch progress (`healthcare/setup/patient_duplicate_check.py`) and for parse failures.
- **No `print`.** The pre-commit `debug-statements` hook blocks leftover `pdb` / `breakpoint` calls.
- **Audit trail**: Frappe document versioning, plus Patient Medical Record entries created on submit through the `patient_history_settings` hooks, act as the clinical activity history.
- **CI-level**: Codecov coverage, CodeQL and Semgrep results.
