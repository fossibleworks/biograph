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
  - healthcare/hooks.py
  - .pre-commit-config.yaml
---

Observability uses only what Frappe provides. There is no external metrics or tracing library.

- **`frappe.log_error(message, title)`** writes to the Error Log doctype. Use it for caught exceptions in integrations, background jobs and patches (about 24 call sites). Pass a descriptive title such as `"Unavailability Calendar Event Error"` and use `frappe.get_traceback()` for the body.
- **`frappe.logger().info/error(...)`** is used sparingly, mostly in patches.
- Frappe's own request, RQ job and scheduler logs cover runtime visibility. CI stores `bench_run_logs.txt` from `bench start`.
- Business audit trails come from Frappe document versioning and the medical record (Patient History) that the global submit/cancel hooks create.
- **Do not log PHI** (patient identifiers or clinical details) in log titles or messages beyond what you need to debug. `detect-secrets` runs in pre-commit to catch credentials.
