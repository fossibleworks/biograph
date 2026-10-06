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
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/healthcare/utils.py
  - healthcare/setup.py
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
  - healthcare/public/js/sales_invoice.js
---

- **Validation errors use `frappe.throw`.** The codebase has about 181 calls. Always pass a translated message, and optionally a title and exception class: `frappe.throw(_("Appointment end must be after start."))`, `frappe.throw(msg, title=_("Missing Configuration"))`, `frappe.throw(_(...), OverlapError)`.
- **Domain exceptions** subclass `frappe.ValidationError` and are defined at the top of the controller module. Examples: `MaximumCapacityError` and `OverlapError` in `patient_appointment.py`, `OverlapError` in `insurance_payor_contract.py`. Tests assert these classes with `assertRaises`.
- **Catch specific Frappe exceptions** when you expect them, e.g. `except frappe.DuplicateEntryError:` in `setup.py`. A broad `except Exception` appears only in patches, uninstall, and non-critical side effects.
- **Non-fatal failures** (notifications, calendar events, patch steps) are recorded with `frappe.log_error(...)` and do not raise to the user: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`. They then appear in the Error Log doctype.
- On the client, desk JS reports problems with `frappe.msgprint(__("..."))` and transient success with `frappe.show_alert({...})`.
- Semgrep (Frappe rules) runs in CI. Suppress a rule with `# nosemgrep` only when it is intentional, e.g. `frappe.throw(message)  # nosemgrep` in compatibility-check patches.
