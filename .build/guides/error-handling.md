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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/public/js/utils.js
---

- **Validation errors:** raise them with `frappe.throw(_("message"), ExcClass?, title=_("..."))`. There are about 181 `frappe.throw` calls in Python code. Messages are always translated with `_()` and use `{0}` placeholders with `.format(...)`.
- **Typed errors:** each module defines its own exceptions by subclassing `frappe.ValidationError` (`OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`). Pass the class to `frappe.throw` so callers and tests can catch it.
- **Missing configuration** errors use `title=_("Missing Configuration")` (`healthcare/healthcare/utils.py`).
- **Non-blocking warnings:** use `frappe.msgprint(_("..."))` to inform without stopping. Desk JS uses `frappe.msgprint(__("..."))` and `frappe.throw` in form scripts.
- **Background or side-effect failures** (calendar events, patches): catch `Exception`, then record it with `frappe.log_error(message_or_traceback, "<Title>")` so it appears in the Error Log, and continue. Patches add `frappe.get_traceback()`.
- **Patches** that must abort use `frappe.throw(message)  # nosemgrep`.
- **API (whitelisted) endpoints** rely on Frappe's standard error serialisation. Raise with `frappe.throw` instead of returning error dicts.
- Avoid broad `except Exception` unless it is followed by `frappe.log_error` (there are about 31 existing sites). Never swallow errors silently.
