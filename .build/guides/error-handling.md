---
title: Error handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Validation errors go to the user through `frappe.throw`** (about 180 call sites). Always translate the message:
```python
frappe.throw(_("Please set {0} in Healthcare Settings").format(...), title=_("Missing Configuration"))
```
- Pass a `title=_()` for a categorised dialog. Use "Missing Configuration" for settings that have not been set.
- When callers or tests need to catch a specific error type, define a subclass of `frappe.ValidationError` in the controller module, as with `MaximumCapacityError` and `OverlapError` in `patient_appointment.py` and `insurance_payor_contract.py`. Raise it with `frappe.throw(msg, OverlapError)`.
- Validation belongs in controller hooks (`validate`, `before_submit`, `on_cancel`) or in the `doc_events` handlers in `hooks.py`, not in the client. The PR template says: "All business logic and validations must be on the server-side."

**Non-fatal failures** in background or side-effect work (SMS, calendar events, notifications, patches) are caught and recorded, so they don't block the transaction:
```python
try:
	...
except Exception:
	frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))
```
The user is then told through `frappe.msgprint(_(...))`.

**Informational messages** use `frappe.msgprint(_("Sales Invoice {0} created").format(...))`.

**Client side:** desk JS shows errors with `frappe.msgprint`/`frappe.throw` and wraps strings in `__()`.

**Do not:**
- swallow exceptions without `frappe.log_error`
- use bare `except:`
- show untranslated messages

If a `frappe.throw` is deliberate in a place Semgrep flags, annotate it with `# nosemgrep`, as in `check_version_compatibility_with_frappe.py`.
