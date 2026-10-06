---
title: Error handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/doctype/item_insurance_eligibility/item_insurance_eligibility.py
---

- **User/validation errors:** `frappe.throw(_("message"), ExcClass?, title=_("Title"))`. This aborts the transaction and shows a dialog. For example: `frappe.throw(_("Appointment end must be after start."))`.
- **Typed errors:** define small domain exceptions that subclass `frappe.ValidationError` at the top of the controller module (`OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`). Pass them to `frappe.throw` so that tests can `assertRaises` them.
- **Non-blocking notices:** `frappe.msgprint(_(...))`, with `alert=True` for toasts (e.g. "Sales Invoice {0} created").
- **Unexpected failures in side work** (calendar events, notifications): catch broadly, then `frappe.log_error(msg, "<Title>")` so the error lands in the Error Log doctype. Keep the main flow running only when the side effect is optional.
- Use `get_link_to_form` in messages to link to the related document.
- Client side: `frappe.throw(__("..."))` / `frappe.msgprint` in form scripts. Validation still has to live on the server.
