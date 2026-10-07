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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/hooks.py
---

There is no metrics or tracing stack. Observability relies on Frappe's built-in facilities:

- **`frappe.log_error(...)`** writes to the Error Log DocType, which is the main way failures are surfaced (about 24 call sites, together with logger calls). Use it in `except` blocks for non-fatal failures and give it a human-readable translated title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- **`frappe.logger().info/error(...)`** is used sparingly, mostly in patches and for parse failures.
- **User feedback:** `frappe.msgprint` for successes or warnings that the user should see ("Sales Invoice {0} created").
- **Audit trail:** Frappe document versioning, plus medical-record creation on submit through the wildcard doc_events.
- Do not log PHI (patient identifiers or clinical details) in error titles. Put context in the message body only when it is needed.
