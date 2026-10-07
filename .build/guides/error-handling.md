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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
---

- **User-facing validation:** `frappe.throw(_("Message {0}").format(value), [ExceptionClass], title=_("..."))`. There are about 180 call sites. Use positional `{0}` placeholders inside `_()` and call `.format` outside it.
- **Typed errors:** define module-level subclasses of `frappe.ValidationError` for conditions that tests or callers need to catch, for example `MaximumCapacityError` and `OverlapError` in `patient_appointment.py`. Raise them with `frappe.throw(msg, OverlapError)`.
- **Permissions:** in whitelisted APIs, raise `frappe.throw(_("Not allowed ..."), frappe.PermissionError)` (see `get_print_format` in the portal API).
- **Missing setup:** use `title=_("Missing Configuration")` when a required setting or item is not configured (see `utils.py`).
- **Non-fatal failures** (SMS, calendar events, background jobs, patches): catch the exception, then call `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(title=...)`. Optionally tell the user with `frappe.msgprint`. Don't swallow exceptions silently.
- **Patches** that must abort an incompatible upgrade use `frappe.throw(message)  # nosemgrep`.
- **JS:** `frappe.throw(__("..."))` and `frappe.msgprint(__("..."))` in form scripts. On the portal, `createResource`/`call` errors show through frappe-ui `<ErrorMessage>`.
