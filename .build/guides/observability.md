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
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - .github/helper/install.sh
---

There is no metrics or tracing stack. Observability relies on Frappe built-ins:

- **The Error Log doctype**, via `frappe.log_error(...)` (about 15 sites). Use it for failures in scheduler jobs, notifications, calendar sync, payment records and patches. Pass a short human title and the traceback (`frappe.get_traceback()`) or the exception message.
- **The `frappe.logger()`** file logger (a few sites) logs `.info`/`.error` progress in setup and patches, e.g. `patient_duplicate_check.py`.
- `print()` appears in some legacy and patch code. Do not add it to runtime paths.
- Background jobs go through `frappe.enqueue`, so they show up in RQ Job and Scheduled Job Log.
- In CI, bench output is captured to `bench_run_logs.txt`, and coverage goes to Codecov.
