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
  - healthcare/healthcare/doctype/item_insurance_eligibility/item_insurance_eligibility.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **Validation failures:** call `frappe.throw(_("message"), title=_("..."))`. There are about 181 occurrences. Messages are translated, and links to configuration go through `get_link_to_form`, for example:
  ```python
  msg = _("Please Configure Clinical Procedure Consumable Item in {0}").format(
  	get_link_to_form("Healthcare Settings", "Healthcare Settings")
  )
  frappe.throw(msg, title=_("Missing Configuration"))
  ```
- **Typed errors:** subclass `frappe.ValidationError` per domain condition (`OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`) and pass the class as `exc=` so callers and tests can catch it specifically.
- **Business rules live on the server.** The PR template says all business logic and validations must be server-side, usually in the controller's `validate()`.
- **Non-fatal / background failures:** catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(title=...)` so it shows in the Error Log doctype, e.g. "Appointment Confirmation Message Not Sent". Do not raise in notifications, scheduler jobs or patches when the main transaction should still succeed.
- **Warnings and info:** `frappe.msgprint(...)` (about 38 uses).
- **Client side:** `frappe.throw` / `frappe.msgprint` with `__()` strings in form scripts.
- When `frappe.throw` is intentionally used where semgrep would flag it, annotate it with `# nosemgrep` (as in the v16 compatibility patch).
