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
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - .github/workflows/codeql.yml
---

# Observability

The app has no metrics or tracing of its own. It relies on Frappe's built-in facilities.

- **Error Log (DB-backed)**: `frappe.log_error(...)` is the main tool (about 15 call sites), used in background jobs, notifications, patches and payment handling. Give it a clear title, for example `"Unavailability Calendar Event Error"` or `_("Appointment Confirmation Message Not Sent")`, and include `frappe.get_traceback()` or the exception.
- **File logger**: `frappe.logger()` (about 9 uses) records progress of setup and patch routines with `.info(...)`/`.error(...)`, for example in `healthcare/healthcare/setup/patient_duplicate_check.py`. Do not use `print`; the pre-commit `debug-statements` hook catches pdb/breakpoint.
- **Realtime UI feedback**: `frappe.publish_realtime` notifies the desk when enqueued jobs finish (sample collection).
- **Audit trail**: DocType versioning and timeline comments come from Frappe (`track_changes` in the DocType JSON).
- **Code quality signals**: Codecov coverage, CodeQL (weekly and on PRs to develop), and semgrep.
