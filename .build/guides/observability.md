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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - .github/workflows/codeql.yml
---

The app has no metrics or tracing stack. It relies on Frappe's built-in facilities:

- **`frappe.log_error(...)`** is the main tool (about 15 call sites). It writes to the *Error Log* doctype, which admins can see in Desk. Pass a short, human-readable title:
  - `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`
  - `frappe.log_error(message=e, title="Failed to mark Collected!")`
  
  Use it for failures in notifications, calendar events, payment records and patches.
- **`frappe.logger()`** is used sparingly (about 9 call sites) for informational and diagnostic lines in setup and patch code, for example `frappe.logger().info("Starting patient duplicate check rules setup")`.
- **User-visible signals** use `frappe.msgprint(..., alert=True, indicator=...)`.
- **Avoid `print()`.** About 75 non-test call sites exist, mostly legacy patches and setup code. New code should use the logger or log_error.
- **CI-side visibility:** Codecov coverage reports, CodeQL (`codeql.yml`), pip-audit and detect-secrets.
