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
  - .github/workflows/codeql.yml
  - .pre-commit-config.yaml
---

# Observability

The app adds no metrics or tracing stack of its own. It uses Frappe's built-in facilities:

- **Error Log doctype** via `frappe.log_error(message, title)` or `frappe.log_error(title=...)`. This is the main way to record unexpected failures in background jobs, patches and integrations, with about 15 call sites. Include `frappe.get_traceback()` when catching broad exceptions, and give a descriptive title (e.g. "Unavailability Calendar Event Error").
- **`frappe.logger()`** for informational logs (e.g. patch success). It is used sparingly.
- External-integration requests are persisted as documents. For example, `ABDM Request` stores request/response for audit.
- Scheduler and background-job status is visible through Frappe's RQ Job / Scheduled Job Log.
- CI security observability: CodeQL (Python and JS, weekly), semgrep, pip-audit, detect-secrets.

Do not use `print()` for diagnostics. The `debug-statements` pre-commit hook blocks leftover debuggers.
