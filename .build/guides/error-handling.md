---
title: Error handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
---

- **Validation errors:** raise them with `frappe.throw(_("Message."), ExcClass)`. There are about 181 `frappe.throw` calls. Messages are translated and usually end with a period. Use `get_link_to_form` or `.format()` to name the record involved.
- **Custom exceptions:** subclass `frappe.ValidationError` at module top, named `<Thing>Error`. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`. Pass the class as the second argument to `frappe.throw` so tests can `assertRaises` it.
- **Non-fatal failures** (notifications, SMS, calendar events, patches): catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("Short Title"))` or `frappe.log_error(title=...)`. Do not re-raise when the main transaction should still succeed (for example, "Appointment Confirmation Message Not Sent").
- **Client side:** use `frappe.msgprint({...})` or `frappe.throw` in form scripts for user feedback. The portal uses frappe-ui dialogs.
- Do not swallow exceptions silently. Every broad `except` should log through `frappe.log_error`.
