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
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Validation errors shown to users**
- Raise them with `frappe.throw(_("Message {0}").format(value), title=_("..."))`. There are about 180 call sites.
- Pass a specific exception class where callers or tests need to tell errors apart.
- Throw from DocType `validate()` and `validate_*` methods. The PR template requires all business logic and validation to run **server-side**.

**Typed errors**
- Declare small subclasses of `frappe.ValidationError` at module top, for example:
  - `OverlapError`, `MaximumCapacityError` in `patient_appointment.py`
  - `CoverageNotFoundError`, `NoActiveContractError` in `patient_insurance_coverage.py`
  - `OverlapError` in `insurance_payor_contract.py`
- Raise them with `frappe.throw(msg, title=..., exc=OverlapError)`.
- Use `title=_("Missing Configuration")` for setup and configuration gaps.
- Add `# nosemgrep` only where a Frappe semgrep rule is knowingly bypassed.

**Non-fatal or background failures** (patches, messaging, scheduler, calendar sync)
- Catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(title=...)`. This writes to the Error Log doctype.
- Optionally tell the user with `frappe.msgprint`.
- Example: SMS failure gives "Appointment Confirmation Message Not Sent".
- Do not swallow exceptions silently.

**Messages:** use `frappe.msgprint(_(...))` for informational feedback, for example "Sales Invoice {0} created".
