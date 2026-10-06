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
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - .pre-commit-config.yaml
---

The app relies on built-in Frappe facilities. There is no metrics or tracing library.

- **Error Log doctype through `frappe.log_error`** is the main mechanism, with about 15 call sites. Pass a traceback or message plus a short, human-readable title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(message=e, title="Failed to mark Collected!")`. Use it for non-fatal failures in notifications, calendar sync, payments and patches.
- **`frappe.logger()`** is used sparingly (about 9 calls), mainly in setup and patches, e.g. `frappe.logger().info("Starting patient duplicate check rules setup")`, and `.error(...)` for parse failures.
- **Realtime user feedback:** `frappe.publish_realtime` (sample collection) and `frappe.msgprint` / `frappe.show_alert` in desk JS.
- **Audit trail:** standard Frappe document versioning and timeline, plus `Patient Medical Record` entries created for clinical events.
- Do not use `print()`. The pre-commit `debug-statements` hook blocks leftover debuggers.
