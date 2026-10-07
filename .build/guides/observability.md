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
  - codecov.yml
---

The project has no dedicated metrics or tracing stack. Observability relies on Frappe's built-in facilities:

- **Error Log doctype through `frappe.log_error`** (about 24 call sites). This is the main mechanism. Pass the traceback and a short, translated, human-readable title:
  ```python
  frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))
  frappe.log_error(error_msg, "Unavailability Calendar Event Error")
  frappe.log_error(title="Error renaming DocType to Time Block Practitioner Availability")
  ```
- **`frappe.logger()`** is used sparingly, mainly in patches, for info and error lines, as in `setup_patient_duplicate_check_rules.py`.
- Background jobs (`frappe.enqueue`) and scheduler events show up in Frappe's RQ Job and Scheduled Job Log.
- **Coverage reporting:** Codecov, on scheduled CI runs.
- **Auditability** comes from Frappe document versioning and Patient Medical Record entries written by the `doc_events` hooks.

**Conventions**
- Log failures in side-effect paths (SMS, notifications, calendar sync, migrations) rather than letting them raise.
- Use a stable, descriptive Error Log title so that entries can be grouped.
- Do not use `print()`. The `debug-statements` pre-commit hook blocks pdb and breakpoint.
- Never log PHI beyond what the Error Log needs. This is a healthcare system.
