---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
---

There is no metrics or tracing stack. Observability relies on Frappe built-ins:
- **`frappe.log_error(message=..., title=...)`** writes to the **Error Log** doctype. Use it for caught exceptions in background, scheduler, and integration code, with a short human-readable title (e.g. "Failed to mark Collected!") and the traceback or exception as the message. About 15 call sites.
- **`frappe.logger()`** (`.info/.debug/.error`) writes to the bench log files. Setup and install routines use it, e.g. `setup/patient_duplicate_check.py`.
- Documents get Frappe's built-in audit trail (version history, `track_changes`). `frappe.publish_realtime` is used once, for live UI updates.
- About 40 stray `print(` calls exist in the Python code. Do not add more; use `frappe.logger()` or `log_error` instead.
