---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - .pre-commit-config.yaml
---

The app has no metrics or tracing library. It relies on Frappe's built-in facilities.

- **`frappe.log_error(message, title)`** is the main convention, with about 15 call sites. It writes an **Error Log** record that admins can see in Desk. Use it for caught exceptions in background jobs, notifications, integrations and patches. Always give a short, descriptive `title` (for example "Can't bill Service Unit occupancy" or "Appointment Confirmation Message Not Sent"), and pass `frappe.get_traceback()` as the message when you need the stack.
- **`frappe.logger()`** with `.info`, `.debug` or `.error` is used for setup and migration progress (e.g. `healthcare/healthcare/setup/patient_duplicate_check.py`, logging rule counts and progress) and for occasional parse failures. Do not use the stdlib `logging` module directly.
- **Realtime**: `frappe.publish_realtime` sends progress to the browser for long jobs (sample collection).
- **Release and CI signals**: Codecov coverage, CodeQL weekly scans, Semgrep, pip-audit and detect-secrets.

Do not leave `print()` statements or debuggers behind. The pre-commit `debug-statements` hook fails on `breakpoint`/`pdb`.
