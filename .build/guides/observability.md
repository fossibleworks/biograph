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
  - patient_portal/src/socket.js
  - .pre-commit-config.yaml
---

There is no external metrics or tracing stack. Observability uses Frappe built-ins:
- **`frappe.log_error(...)`** writes to the Error Log doctype and is the main mechanism (about 24 call sites). Pass a traceback with a translatable title, `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`, or `title=`.
- **`frappe.logger()`** (`.info` / `.error`) for non-fatal diagnostics, e.g. unparseable appointment times, or patch progress.
- **`frappe.publish_realtime`** / `frappe.msgprint` for user-visible progress. The portal listens over socket.io (`patient_portal/src/socket.js`).
- In CI, bench output goes to `bench_run_logs.txt`. Coverage goes to Codecov.

Don't add `print()`: the pre-commit `debug-statements` hook and the Frappe semgrep rules flag debug code.
