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
  - healthcare/setup.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - patient_portal/src/components/BookAppointmentModel.vue
---

# Error handling

## Validation errors (user-facing)
- Raise with **`frappe.throw(_("message {0}").format(value))`**. There are about 180 call sites, and this is the standard way to stop a save, submit, or API call.
- When callers or tests need to tell an error apart, define a module-level subclass of `frappe.ValidationError` and pass it as the second argument. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`.
- For permission failures, use `frappe.throw(_("Not permitted"), frappe.PermissionError)`.
- Use `frappe.msgprint(..., alert=True)` for non-blocking notices.

## Background/side-effect failures
- Side effects that must not block the main transaction, such as calendar events, SMS/notification sending, and patches, go in `try/except Exception` and are recorded with **`frappe.log_error(frappe.get_traceback(), _("Title"))`** or `frappe.log_error(title=...)` (Error Log doctype).
- Expected duplicates in setup/install are caught narrowly (`except frappe.DuplicateEntryError`).
- Avoid `print()` for errors (one legacy occurrence exists in patient_appointment). Use `frappe.log_error` instead.

## Client side
- Desk relies on Frappe's server message dialogs.
- In the Patient Portal, frappe-ui `createResource` `onError(e)` handlers show `e.messages?.[0] || e` through `<ErrorMessage>` or `toast`.
