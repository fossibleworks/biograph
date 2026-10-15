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
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - healthcare/healthcare/doctype/abdm_request/abdm_request.py
  - .pre-commit-config.yaml
---

The app relies only on Frappe's built-in facilities. There are no metrics or tracing libraries.

- **`frappe.log_error(message, title)`** (about 24 call sites) writes to the **Error Log** DocType. It is the main way to record failures in background jobs, notifications, billing side effects and calendar integration. Pass `frappe.get_traceback()` as the message and a short, human-readable (often translated) title, e.g. `"Can't bill Service Unit occupancy"`, `"Unavailability Calendar Event Error"`.
- **`frappe.logger().error(...)`** is used sparingly for parse-level warnings (e.g. unparseable appointment times).
- Integration requests (ABDM) are stored as records (`ABDM Request` doctype), which gives you an audit trail of external calls.
- Document history comes from Frappe's versioning/timeline (track_changes on doctypes).
- CI keeps `bench_run_logs.txt` from the bench process for debugging.

Don't use `print()` in server code. pre-commit's `debug-statements` hook rejects leftover debugger calls.
