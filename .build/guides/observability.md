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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/hooks.py
  - .pre-commit-config.yaml
---

# Observability

The app adds no metrics or tracing stack of its own. It relies on Frappe's built-in facilities.

- **`frappe.log_error(...)`** writes to the Error Log doctype and is the main way to record failures. There are about 15 call sites, mostly in patches and in background or notification paths such as appointment confirmation messages and unavailability calendar events. Pass a clear, translatable title: `frappe.log_error(frappe.get_traceback(), _("<What failed>"))` or `frappe.log_error(title=...)`.
- **`frappe.logger()`** is used sparingly, about 9 times, for informational or parse warnings, for example `frappe.logger().error(f"Could not parse appointment time: {appt_time_str}")`.
- **Realtime events** go through `frappe.publish_realtime` (for example in sample collection). Long work goes through `frappe.enqueue`, and those jobs show up in Frappe's RQ job views.
- Scheduled jobs are declared in `scheduler_events` in `hooks.py` and appear in the Scheduled Job Log.
- Do not use `print()` or leftover debug statements. The pre-commit `debug-statements` hook rejects them.
