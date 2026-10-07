---
title: Error handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
---

- **Validation errors:** raise with `frappe.throw(_("Message {0}").format(value), title=_("Short Title"))`. There are about 180 throws, and titles are common, e.g. "Missing Configuration", "Not Available", "Customer Not Found". Pass an exception class when it matters, e.g. `frappe.throw(_("Not allowed to print this document."), frappe.PermissionError)`.
- **Custom exceptions:** subclass `frappe.ValidationError` at the top of the controller module, e.g. `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`. Pass them via `exc=` so tests can `assertRaises` them.
- **Non-blocking notices:** `frappe.msgprint(..., indicator="warning"|"error", title=...)` (about 38 uses).
- **Background or side-effect failures** (notifications, calendar events, patches): catch the error, then call `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(title=...)` so the main transaction can continue. Example: appointment confirmation messages in `patient_appointment.py`.
- **Translation:** format after translating: `_("{0} is a holiday").format(date)`. Do not use `_("...".format())`; one existing instance does this wrong.
- **Portal API:** whitelisted methods raise through `frappe.throw`. The frappe-ui resources surface the message, and `ErrorMessage`-style components render `error`.
- Patches that must abort deliberately use `frappe.throw(message)  # nosemgrep`.
