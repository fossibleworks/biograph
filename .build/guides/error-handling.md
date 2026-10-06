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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/setup.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - patient_portal/src/components/Payment.vue
---

- **User/validation errors:** raise with `frappe.throw(_("message {0}").format(x), title=_("Title"), exc=SomeError)`. This is the dominant pattern (about 180 call sites). Messages are translatable and title-cased titles such as `_("Missing Configuration")` are common.
- **Domain exception classes** subclass `frappe.ValidationError` and are defined at the top of the doctype module. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`. Pass them as the second argument to `frappe.throw` so tests can `assertRaises` them.
- **Non-blocking notices:** use `frappe.msgprint(...)`.
- **Unexpected failures in background or side-effect paths** (notifications, calendar events, patches): catch broadly and record with `frappe.log_error(frappe.get_traceback(), _("Short Title"))` or `frappe.log_error(title=...)` so the main transaction continues. See the appointment confirmation and unavailability calendar event handling in `patient_appointment.py`.
- **Idempotent setup:** catch specific errors like `frappe.DuplicateEntryError` in `setup.py`.
- **API endpoints:** whitelisted methods raise via `frappe.throw` too. Frappe turns these into the standard error response, and the portal shows `ErrorMessage` components with the server message.
- Avoid bare `print()` in app code (it appears mostly in patches/setup). Use `frappe.log_error` or `frappe.logger()` instead.
