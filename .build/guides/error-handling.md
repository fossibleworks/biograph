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
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
---

# Error handling

## Validation errors (server)
- Raise user-facing errors with **`frappe.throw(_("..."))`**. There are about 180 calls on the Python side. Pass a `title=` for categorised errors, for example `frappe.throw(msg, title=_("Missing Configuration"))`.
- Put links to related records in messages with `get_link_to_form(...)`, for example "Please Configure ... in {0}" linking to Healthcare Settings.
- Domain error types subclass `frappe.ValidationError` and are defined at the top of the controller module. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`. Pass them as `exc=` so tests can `assertRaises` them.
- Run validation in controller hooks (`validate`, `before_submit`, `on_cancel`) or in `doc_events` from `hooks.py`.
- Use `frappe.msgprint` for non-blocking notices.

## Catching exceptions
- Catch specific Frappe exceptions where possible, for example `except frappe.DuplicateEntryError:` in setup.
- Broad `except Exception` belongs only in background or notification paths and in patches, and it must log. Example: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- Patches catch failures and call `frappe.log_error(title=...)` so a migrate does not abort.

## Client side
- JS form scripts use `frappe.throw(__("..."))` and `frappe.msgprint` for client-side guards. The server stays the source of truth.
