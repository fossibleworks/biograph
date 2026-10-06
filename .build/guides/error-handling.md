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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/public/js/utils.js
  - patient_portal/src/components/Payment.vue
---

- **User-facing validation:** use `frappe.throw(_("message"), [ExcClass], title=_("Title"))` (about 181 call sites). Wrap the message in `_()` and highlight values with `frappe.bold()`. Pass `title=` for categorised errors (e.g. `title=_("Missing Configuration")`).
- **Domain error classes:** subclass `frappe.ValidationError` inside the doctype module, e.g. `OverlapError` and `MaximumCapacityError` in `patient_appointment.py`, and `OverlapError` in `insurance_payor_contract.py`. Pass the class to `frappe.throw` so tests can assert on it.
- **Background or non-fatal failures:** for scheduler jobs, notifications, calendar events and patches, catch the exception and call `frappe.log_error(...)` instead of raising. The preferred form is `frappe.log_error(frappe.get_traceback(), _("Short Title"))` or `frappe.log_error(message=..., title=...)`, which writes to the Error Log doctype.
- Avoid bare `except Exception:` that swallows errors without logging (there are about 31 broad catches, a legacy pattern).
- **Desk JS:** use `frappe.msgprint(__("..."))` for user feedback, and `frappe.throw` in form validation.
- **Portal:** render frappe-ui `ErrorMessage` with the resource error.
