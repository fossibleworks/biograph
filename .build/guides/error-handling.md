---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - patient_portal/src/components/BookAppointmentModel.vue
---

# Error handling

- **Validation errors:** use `frappe.throw(_("message {0}").format(...), title=_("Title"))` (about 180 uses). Pass an exception class for domain errors, e.g. `frappe.throw(msg, OverlapError)`. Use a title for configuration problems (`title=_("Missing Configuration")`, `_("Customer Not Found")`).
- **Custom exceptions:** subclass `frappe.ValidationError` at the top of the controller module (`MaximumCapacityError`, `OverlapError`). Tests assert on these classes.
- **Bold and links in messages:** `frappe.bold(value)` and `get_link_to_form(doctype, name)`.
- **Non-blocking notices:** `frappe.msgprint(_(...), alert=True)`, e.g. "Sales Invoice {0} created".
- **Best-effort side effects** (notifications, calendar events, patches): wrap them in `try/except` and record the failure with `frappe.log_error(frappe.get_traceback(), _("Short Title"))` or `frappe.log_error(title=...)`, so the main transaction can continue. Examples: "Appointment Confirmation Message Not Sent", "Unavailability Calendar Event Error".
- **Whitelisted APIs** raise through `frappe.throw` and Frappe turns that into the JSON error response. The Vue portal shows it with `toast.error(err.messages?.[0] || err)`.
- Do not swallow exceptions silently. Do not raise bare `Exception`.
