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
  - .pre-commit-config.yaml
  - healthcare/hooks.py
---

# Observability

This project relies on the Frappe framework's built-in observability. It has no metrics or tracing libraries.

- **Error Log doctype** via `frappe.log_error(...)` is the primary sink, with about 15 call sites. The convention is `frappe.log_error(frappe.get_traceback(), _("Human Title"))` or `frappe.log_error(title=..., message=...)`. Titles are short, translated descriptions such as "Appointment Confirmation Message Not Sent" and "Unavailability Calendar Event Error".
- **`frappe.logger()`** is used sparingly (about 9 call sites, mostly patches and appointment time parsing) for info and error lines in the site logs.
- **Audit trail**: Frappe version tracking and comments. The app also builds a clinical timeline, Patient Medical Record, through the wildcard `doc_events` hooks.
- No `print()` debugging. The pre-commit `debug-statements` hook blocks `pdb`/breakpoints.
- CI keeps `bench_run_logs.txt` during test runs.
