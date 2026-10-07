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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - .github/workflows/ci.yml
---

The app has no metrics or tracing library. It relies on Frappe's built-in facilities:

- **`frappe.log_error(message_or_traceback, title)`** writes to the Error Log DocType. This is the main convention (about 24 call sites, together with logger calls) for caught exceptions in controllers, background jobs and patches. Give it a descriptive title, for example `"Unavailability Calendar Event Error"`.
- **`frappe.logger().info/error(...)`** is used in a few patches for progress and failure messages.
- **Background jobs** (`frappe.enqueue`, `scheduler_events`) are monitored through Frappe's RQ Job / Scheduled Job Log.
- **CI coverage** is reported to Codecov.

When adding error logging, catch the exception, call `frappe.log_error(frappe.get_traceback(), "<Feature> Failed")`, and only swallow it when the user flow must continue.
