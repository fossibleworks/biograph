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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - .pre-commit-config.yaml
---

There is no metrics or tracing stack. Observability uses Frappe's built-in tools only.

- **`frappe.log_error(...)`:** the main mechanism, used about 15 times. It writes to the Error Log DocType. Pass a traceback (`frappe.get_traceback()`) or a message, plus a human-readable title (often wrapped in `_()`).
- **`frappe.logger()`:** used occasionally (`.info` / `.error`) in setup code and patches, e.g. `healthcare/healthcare/setup/patient_duplicate_check.py`.
- **Do not use `print`.** The pre-commit `debug-statements` hook blocks `pdb` and `breakpoint` calls.
- CI keeps bench output in `bench_run_logs.txt`.
