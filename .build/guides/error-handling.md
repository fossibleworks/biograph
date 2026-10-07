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
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
  - healthcare/permissions.py
---

# Error handling

## Validation errors (user-facing)
- Use **`frappe.throw(_("Message {0}").format(value), [ExcClass], title=_("Title"))`**. This pattern appears about 180 times. Do not raise raw Python exceptions from controllers.
- To give a distinct error type, subclass **`frappe.ValidationError`** in the controller module, for example `OverlapError` and `MaximumCapacityError` in patient_appointment, or `CoverageNotFoundError` and `NoActiveContractError` in patient_insurance_coverage. Pass the class as the second argument to `frappe.throw`, so tests can use `assertRaises(OverlapError, ...)`.
- Use the `title=` argument for categories such as `_("Missing Configuration")` or `_("Not Available")`.
- Use `get_link_to_form(doctype, name)` inside messages to point users to the record involved.
- For non-blocking warnings, use `frappe.msgprint` (about 38 uses).

## Background and integration failures
- In scheduled jobs, notifications and patches, catch the exception and call **`frappe.log_error(...)`**. This creates an Error Log record and keeps the job going. Prefer `frappe.log_error(title=..., message=frappe.get_traceback())`.
  - Examples: appointment confirmation SMS failure, calendar event cancellation, sample collection, payment record.
- Patches that might fail on some sites should catch, log, and continue (`patches/v16_0/rename_time_block_to_practitioner_availability.py`).
- Version-compatibility patches deliberately use `frappe.throw` with `# nosemgrep`.

## API endpoints
- `@frappe.whitelist()` methods rely on Frappe's standard error envelope: a thrown ValidationError becomes `exc_type` plus `_server_messages`. Do not build custom error JSON.
- The portal displays errors with frappe-ui `ErrorMessage`.
