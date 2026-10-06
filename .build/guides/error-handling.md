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
  - healthcare/healthcare/doctype/item_insurance_eligibility/item_insurance_eligibility.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
---

- **Validation errors seen by users:** raise them with `frappe.throw(_("..."))`, which has about 180 uses in Python. Pass a `title=_(...)` for categorised dialogs (e.g. `title=_("Missing Configuration")`). Pass a specific exception class when callers or tests need to tell errors apart, e.g. `frappe.throw(msg, OverlapError)`.
- **Custom exceptions:** define them at module level as `class XError(frappe.ValidationError): pass` in the DocType controller. Existing examples are `OverlapError`, `MaximumCapacityError` and `CoverageOverlapError`.
- **Messages:** always translate them, and highlight values with `frappe.bold()`. For non-blocking warnings use `frappe.msgprint` (about 38 uses).
- **Background or side-effect failures** (notifications, calendar events, patches): catch them so the main transaction can finish, and record them with `frappe.log_error(frappe.get_traceback(), _("<Short Title>"))` or `frappe.log_error(title=...)`. Example: "Appointment Confirmation Message Not Sent". Do not swallow errors silently. Use bare `except Exception` only around these side effects (about 31 occurrences exist).
- **Desk JS:** use `frappe.throw` / `frappe.msgprint` for blocking feedback and `frappe.show_alert` for transient feedback.
- **Portal (Vue):** show server errors as `toast.error(err.messages?.[0] || err)` from frappe-ui.
- **Patches:** compatibility guards call `frappe.throw(message)  # nosemgrep`. Add a `# nosemgrep` annotation only with a reason.
