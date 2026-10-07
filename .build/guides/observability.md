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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - .pre-commit-config.yaml
---

This app adds no metrics or tracing. It relies on Frappe's built-in mechanisms:

- **Error Log doctype** through `frappe.log_error(...)`. This is the main channel, with about 15 call sites. Pass a short human title, often translated, and the traceback: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`. Use it for background, scheduler, integration (SMS, calendar) and patch failures.
- **The file logger** `frappe.logger().info(...)` / `.error(...)` appears in only a few places: setup and patches (`setup/patient_duplicate_check.py`, `patches/v15_0/setup_patient_duplicate_check_rules.py`) and appointment time parsing.
- **Integration request logs**: ABDM calls are stored as `ABDM Request` documents, a doctype under `healthcare/healthcare/doctype/abdm_request`.
- **Coverage** reports go to Codecov from nightly CI.
- Do not add `print()` debugging. The pre-commit `debug-statements` hook blocks `pdb` and breakpoints.
