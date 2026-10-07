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
---

Observability relies on Frappe built-ins only. There is no metrics or tracing library.

- **`frappe.log_error(message_or_traceback, title)`** (15 uses) writes to the Error Log doctype. Use it for caught exceptions in side-effects and patches. Give it a short human-readable title, translated with `_()` where it is user-visible.
- **`frappe.logger().info/error(...)`** (9 uses) writes to bench log files. It is used in setup and patch flows (patient duplicate check setup, time parsing).
- **`frappe.msgprint`** with `indicator="orange"` tells the user about a degraded but non-fatal outcome.
- Avoid `print()` for diagnostics.
