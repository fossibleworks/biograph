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
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - .pre-commit-config.yaml
---

- The app has no metrics or tracing stack. Observability relies on Frappe built-ins.
- **Error Log:** `frappe.log_error(...)` is the main mechanism (about 15 sites). Pass a human-readable, translatable title, e.g. `_("Appointment Confirmation Message Not Sent")`, plus the traceback (`frappe.get_traceback()`) or a message. Entries appear in the Error Log doctype.
- **Logger:** `frappe.logger().info/error(...)` is used sparingly (about 9 sites), mainly in setup and patch code (`healthcare/healthcare/setup/patient_duplicate_check.py`).
- **Realtime:** `frappe.publish_realtime` notifies the UI about background job progress or completion.
- Do not add `print()` or debugging statements. The pre-commit `debug-statements` hook rejects breakpoints and pdb.
