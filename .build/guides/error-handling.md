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
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
---

- **User/validation errors:** raise with `frappe.throw(_("message"), [ExcClass], title=_("Title"))`. There are about 181 call sites. Messages are translated and often formatted: `_("... {0}").format(frappe.bold(x))`. Titles are short Title Case labels such as `Missing Configuration`, `Invalid Healthcare Service Unit`, `Customer Not Found` and `Practitioner Schedule Not Found`.
- **Custom exceptions:** define small subclasses of `frappe.ValidationError` at module top (`class OverlapError(frappe.ValidationError): pass`, `MaximumCapacityError`) and pass them to `frappe.throw` so tests can assert on them.
- **Non-blocking notices:** use `frappe.msgprint(...)`, with `alert=True` for toast-style confirmations (for example, `_("Sales Invoice {0} created")`).
- **Background or side-effect failures** (notifications, calendar events, patches): catch the exception and call `frappe.log_error(frappe.get_traceback(), _("Title"))` (or `frappe.log_error(title=...)`). Don't let these break the main transaction.
- `B904` (raise from) is ignored by ruff, so plain re-raise is accepted.
- Semgrep (Frappe rules) runs in CI. Use `# nosemgrep` only with justification, as in `check_version_compatibility_with_frappe.py`.
- Validation lives in the server-side controller `validate`/`before_submit` hooks, not only in JS.
