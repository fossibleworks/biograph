---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/www/patient-portal/index.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/public/js/utils.js
  - patient_portal/src/components/BookAppointmentModel.vue
---

# Error handling

## Server (Python)
- **Validation errors** use `frappe.throw(_("message {0}").format(...))`. This raises `frappe.ValidationError` and rolls back the request. It is used about 180 times.
- **Typed errors**: domain-specific subclasses of `frappe.ValidationError` are declared at the top of the controller module and passed as the second argument to `frappe.throw`:
  ```python
  class OverlapError(frappe.ValidationError):
  	pass
  frappe.throw(_("..."), title=_("Appointments Overlapping"), exc=OverlapError)
  ```
  Examples: `MaximumCapacityError`, `OverlapError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`. Tests assert on these with `assertRaises`.
- **Permission and not-found errors** use the Frappe exception classes, for example `frappe.throw(_("Not allowed to print this document."), frappe.PermissionError)` and `frappe.DoesNotExistError` in portal pages.
- **Background and non-critical failures** (scheduler jobs, notifications, calendar events, billing of occupancy) are caught and logged with `frappe.log_error(...)`, which writes an Error Log, so the main transaction continues. Give a clear title, for example `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- Use `frappe.get_link_to_form` in messages to link the user to the conflicting document.
- Do not swallow exceptions in user-triggered flows. Let `frappe.throw` surface them.

## Whitelisted API responses
- Endpoints return plain dicts and lists, and signal errors by raising (`frappe.throw`). Frappe serializes these into `exc_type` and `_server_messages`. There is no custom error envelope.

## Desk JS
- Use `frappe.throw(__(...))` for blocking client-side checks and `frappe.msgprint(__(...))` for informational errors. Wrap strings in `__()`.

## Patient Portal (Vue)
- Each frappe-ui `createResource` has an `onError(e)` that stores `e.messages?.[0] || e` in a reactive `error` ref, which is rendered with the frappe-ui `ErrorMessage` component.
