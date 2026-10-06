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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - .github/helper/install.sh
---

- There is no external metrics or tracing stack. Observability relies on Frappe built-ins:
  - **Error Log doctype** via `frappe.log_error(message_or_traceback, title)`. This is the main convention: there are about 24 log calls, mostly in patches and background or calendar code. Give the error a short, descriptive title (e.g. "Unavailability Calendar Event Error") and pass `frappe.get_traceback()` when you catch an exception.
  - **`frappe.logger()`**: `.info` and `.error` are used occasionally in patches.
- Scheduler failures surface in Frappe's Scheduled Job Log and Error Log.
- **Avoid `print()`** in server code. About 75 non-test `print(` calls exist, mostly in patches and setup. New code should use `frappe.log_error` or `frappe.logger()` instead.
- CI writes `bench_run_logs.txt`, and coverage goes to Codecov on scheduled runs.
