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
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - healthcare/healthcare/doctype/medication_request/medication_request.py
---

# Error handling

## Validation errors (the main mechanism)
- Use `frappe.throw(_("Message"), ExcType)` for user-facing validation failures (~181 call sites). Frappe turns these into an HTTP error response and a Desk dialog, and rolls back the transaction.
- For domain-specific failures, define a module-level exception that subclasses `frappe.ValidationError`, e.g. `class OverlapError(frappe.ValidationError): pass`. Pass it as the second argument (`frappe.throw(msg, OverlapError)`) so tests and callers can catch it precisely. Existing examples: `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`, `CoverageOverlapError`.
- Messages are short sentences, translated with `_()`, with `{0}` placeholders filled through `.format()` and links via `frappe.bold`/`get_link_to_form`.
- Use `frappe.msgprint` for non-blocking notices.

## Catching
- Catch specific Frappe exceptions where an outcome is expected: `frappe.DuplicateEntryError`, `frappe.DoesNotExistError`, `json.decoder.JSONDecodeError`.
- Use `except Exception` only around side effects that must not block the main transaction (notifications, calendar events, payment records). Log with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(msg, "Title")` and continue, so the error appears in the Error Log doctype.
- Do not swallow errors silently. Either re-throw through `frappe.throw` or record them in the Error Log.

## Client side
- Desk JS uses `frappe.msgprint`/`frappe.throw` with `__()` strings and `frappe.confirm` for destructive actions.
