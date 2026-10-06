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
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/healthcare/utils.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
---

**User-facing validation:** raise with `frappe.throw(_("message"))` from controller `validate` and `before_submit` hooks or whitelisted methods. The codebase has about 181 calls. Pass `title=_("...")` for grouped errors (for example `title=_("Missing Configuration")`) and pass an exception class when callers or tests need to catch it.

**Custom exception types** subclass `frappe.ValidationError` and are declared at module top, for example `class OverlapError(frappe.ValidationError)` and `class MaximumCapacityError(frappe.ValidationError)` in patient_appointment and insurance_payor_contract. Tests assert on `frappe.ValidationError` or the subclass.

**Background and non-blocking failures:** catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)`. Examples are appointment confirmation messages that failed to send and calendar event errors. Don't fail the user transaction for side effects like notifications. Patches wrap risky steps the same way.

**Client side:** use `frappe.throw(__(...))` and `frappe.msgprint(__(...))` for blocking problems, and `frappe.show_alert({message, indicator})` for transient feedback.

**API:** whitelisted endpoints return plain data or `None` and rely on Frappe to serialise `frappe.throw` into the standard error response. There is no custom error envelope.

Avoid a bare `except Exception` that swallows errors silently (there are about 31 existing occurrences). Always log with `frappe.log_error`.
