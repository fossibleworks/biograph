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
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - eslint.config.mjs
  - .pre-commit-config.yaml
---

Observability uses Frappe's built-ins only. There is no metrics or tracing library.

- **Error Log:** `frappe.log_error(message_or_traceback, title)` is the main mechanism (~24 uses). Give it a short human title such as "Can't bill Service Unit occupancy" or "Appointment Confirmation Message Not Sent", and pass `frappe.get_traceback()` as the message.
- **Logger:** `frappe.logger().info/error(...)` appears occasionally (patient duplicate check setup, appointment time parsing).
- **Avoid:** ~39 stray `print(` calls and ~22 `console.log` calls exist. ESLint warns on `no-console`, and pre-commit `debug-statements` blocks `pdb`/breakpoints. Don't add new ones.
- **Audit:** document history and medical records are produced by the Patient History Settings hooks. Rely on Frappe versioning instead of custom audit logs.
- **CI logs:** the bench output goes to `bench_run_logs.txt` in CI.
