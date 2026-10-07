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
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - .pre-commit-config.yaml
---

- There is no metrics or tracing stack. Observability relies on **Frappe built-ins**.
- **`frappe.log_error(message_or_traceback, title)`** writes to the Error Log DocType. It is the main way to record failures (about 15 call sites). Use a short, human-readable title (translated with `_()` where existing code does) and include `frappe.get_traceback()` or the relevant document name in the message.
- **`frappe.logger()`** (`.info`/`.error`) is used sparingly for patch/setup progress and parse warnings.
- Background jobs (`frappe.enqueue`) and scheduler events show up in Frappe's RQ Job / Scheduled Job Log. Don't add custom logging infrastructure.
- No `print` statements (pre-commit `debug-statements`). Don't log PHI (patient identifiers and clinical details) beyond the document name needed to debug.
