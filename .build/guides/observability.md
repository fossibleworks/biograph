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
  - .github/workflows/codeql.yml
  - .pre-commit-config.yaml
---

# Observability

There is no external metrics or tracing stack. The app relies on Frappe's built-in facilities:

- **`frappe.log_error(...)`** (about 15 uses) writes to the **Error Log** doctype. This is the main way failures are recorded. Pass a traceback plus a short translated title: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- **`frappe.logger()`** (about 9 uses) writes file logs for setup and patch progress: `frappe.logger().info("Starting patient duplicate check rules setup")` and `.error(...)` for parse failures.
- **Audit trail.** Patient medical-record history comes from the `doc_events` hooks (Patient History Settings). Status fields (`status`, `submitted_date`) are set with `db_set` on lifecycle events.
- **CI-level signals:** Codecov coverage, CodeQL (python and javascript), and Semgrep.

Do not use `print()` for diagnostics. The `debug-statements` pre-commit hook blocks debugger calls.
