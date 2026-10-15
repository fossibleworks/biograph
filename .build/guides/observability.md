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
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - eslint.config.mjs
---

There are no metrics or tracing libraries. Observability relies on Frappe's built-in facilities:

- **`frappe.log_error(...)`** (about 15 uses) writes to the **Error Log** doctype. It is the main way failures in background or side-effect code are recorded. Pass a descriptive `title`, plus the traceback or exception as the message: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- **`frappe.logger()`** writes to bench log files. It is used for setup and migration progress at `info`/`debug` and for parse failures at `error`. Examples are `setup/patient_duplicate_check.py` and the v15 patch `setup_patient_duplicate_check_rules`.
- Scheduled jobs show up in Frappe's Scheduled Job Log, and CodeQL and Semgrep give security visibility in CI.
- **JS:** ESLint warns on `console.*` (`no-console: warn`). Don't leave `console.log` in desk or portal code. Report user-visible problems with `frappe.msgprint`/`frappe.throw` instead.
- Don't log PHI (patient-identifying clinical data) in log messages. Log document names and IDs instead.
