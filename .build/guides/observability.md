---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/uninstall.py
---

# Observability

There is no metrics or tracing stack. The app relies on Frappe built-ins:

- **`frappe.log_error(title=..., message=...)`** writes to the Error Log doctype, visible in Desk. It is the primary way to record failures in background jobs, integrations and notifications (about 15 call sites). Give it a descriptive `title` that includes the document name, plus `frappe.get_traceback()` as the message.
- **`frappe.logger()`** writes to the bench log files. It is used sparingly for info/debug in setup routines (`healthcare/healthcare/setup/patient_duplicate_check.py`) and for parse errors.
- `print()` appears only in install, uninstall and migrate scripts for console output.
- Integration request records such as `ABDM Request` capture external API calls for auditing.
- Scheduler jobs are registered in `hooks.py`. Their failures surface through the Frappe Scheduled Job Log.
