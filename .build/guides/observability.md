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

Observability relies only on Frappe's built-in facilities. There is no metrics or tracing library.

- **`frappe.log_error`** writes to the Error Log doctype. It is the main way failures in background and side-effect code get recorded (about 15 call sites). Use a human-readable, translated title and include `frappe.get_traceback()` in the message.
- **`frappe.logger()`** has a few `.info`/`.error` calls in setup and patch code, plus one parse failure in `patient_appointment.py`. It goes to bench log files.
- **Realtime progress:** `frappe.publish_realtime` for long-running jobs.
- **Coverage reporting:** Codecov on non-PR CI runs.
- About 39 stray `print(` calls exist, mostly in setup and patches. The `debug-statements` pre-commit hook guards against debugger leftovers. Prefer `frappe.logger()` over `print` in new code.
