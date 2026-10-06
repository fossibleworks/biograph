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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - .pre-commit-config.yaml
---

# Observability

There is no dedicated metrics or tracing stack. The app relies on Frappe's built-in facilities:

- **Error Log doctype**: `frappe.log_error(frappe.get_traceback(), _("Human title"))` or `frappe.log_error(title=..., message=...)`. This is the main way failures in background or side-effect code get recorded (about 15 call sites). Give each one a clear, searchable title, such as "Appointment Confirmation Message Not Sent" or "Unavailability Calendar Event Error".
- **`frappe.logger()`**: occasional `.info()` and `.error()` calls, mainly in patches and parsing helpers.
- **Background jobs**: enqueued jobs show up in Frappe's RQ Job / Scheduled Job Log. Scheduler jobs are declared in `hooks.py`.
- **Audit trail**: Patient Medical Record entries are created through the wildcard doc_events. Frappe document versioning provides change history.
- **Coverage and security signals**: Codecov, CodeQL and semgrep in CI.

Do not add `print()` statements. The `debug-statements` pre-commit hook blocks debugger calls.
