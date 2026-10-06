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
  - healthcare/regional/india/abdm/utils.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

Follow the Frappe conventions already used here:

- **Validation errors**: `frappe.throw(_("Message {0}").format(value))`, with about 180 call sites.
  - Pass `title=` for context where useful, e.g. `frappe.throw(title="Not Configured", msg=...)`.
  - Keep business-rule validation on the server, in `validate`/`before_submit` controller hooks. The PR template states that "All business logic and validations must be on the server-side".
- **Typed errors**: subclass `frappe.ValidationError` near the controller and pass the class to `frappe.throw(..., exc=OverlapError)` so tests and callers can catch it. Existing examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`.
- **Non-fatal user notices**: `frappe.msgprint(...)`, with about 38 sites.
- **Background/unexpected failures**: catch, then record with `frappe.log_error(title=..., message=...)`, which writes to the Error Log doctype. Examples are patches and the Sample Collection status update. Do not swallow exceptions silently.
- Markup in messages: older messages use `<b>Field</b>` inside translated strings. Keep the format placeholders inside `_()`.
- Whitelisted APIs rely on Frappe returning the thrown message to the client. The portal and desk JS display it, and they do not build custom error envelopes.
- Avoid bare `except Exception` (about 31 exist). If you need one, log with `frappe.log_error` and re-raise or `frappe.throw` with a user-facing message.
