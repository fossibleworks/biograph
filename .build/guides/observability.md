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
  - .pre-commit-config.yaml
---

There is no metrics or tracing stack. Observability uses the Frappe built-ins:

- **`frappe.log_error(...)`** writes to the Error Log doctype and is the primary convention (about 15 sites). Pass the traceback (`frappe.get_traceback()`) and a short, translatable title, for example `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(title="Error renaming DocType ...")`.
- **`frappe.logger().info/error(...)`** writes to file logs, used sparingly (about 9 sites), mostly in patches and in parsing fallbacks.
- Do not use `print()` or `debug-statements`. The pre-commit `debug-statements` hook blocks pdb and breakpoints.
- Background and scheduled jobs show up in Frappe's RQ Job and Scheduled Job Log. CI captures `bench_run_logs.txt`.
