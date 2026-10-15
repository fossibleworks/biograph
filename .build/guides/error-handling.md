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
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/controllers/service_request_controller.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/utils.py
---

## User-facing validation errors
- Raise them with **`frappe.throw(_("message"), [ExceptionClass], title=_("Title"))`**. There are about 181 call sites. Messages are translated and use `{0}` placeholders through `.format()`. Don't build f-strings inside `_()`: some legacy code does, but it breaks translation extraction.
- Domain-specific errors subclass **`frappe.ValidationError`** and are declared at the top of the controller module. Examples: `OverlapError`, `MaximumCapacityError` (patient_appointment), `CoverageNotFoundError`, `NoActiveContractError` (patient_insurance_coverage), `CoverageOverlapError`. Pass the class as the second argument to `frappe.throw` so callers and tests can catch it.
- For permission failures, pass `frappe.PermissionError` (e.g. `api/patient_portal.py`).
- For non-blocking notices, use `frappe.msgprint(..., alert=True)`.

## Catching
- Catch specific Frappe exceptions where you can (`frappe.DoesNotExistError`, `frappe.exceptions.DuplicateEntryError`), then re-throw a translated, user-friendly message.
- Background or side-effect work (scheduler billing, notifications, calendar events) catches `Exception` and records it with **`frappe.log_error(message=..., title=...)`** or `frappe.log_error(frappe.get_traceback(), _("..."))` so the main transaction isn't blocked.
- Avoid bare `except Exception: pass`.

## Client side
JS form scripts show errors with `frappe.throw` / `frappe.msgprint`. Real validation must also exist on the server.
