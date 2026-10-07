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
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
---

There are no metrics or tracing libraries. Observability goes through Frappe built-ins:

- **`frappe.log_error(...)`** writes to the Error Log doctype and is the main mechanism, used about 15 times. It is usually called as `frappe.log_error(frappe.get_traceback(), _("Human Title"))` or `frappe.log_error(message=..., title=...)`. Give it a stable, descriptive title such as "Unavailability Calendar Event Error" or "Appointment Confirmation Message Not Sent".
- **`frappe.logger().info/error(...)`** is used sparingly, about 9 times, mostly in setup and patches (e.g. patient duplicate-check setup) and for parse failures.
- **User-visible signals:** `frappe.msgprint(..., indicator="orange")` or `alert=True` show soft failures.
- **CI-side:** Codecov coverage and CodeQL scans.
