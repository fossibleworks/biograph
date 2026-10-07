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
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
---

- **Validation errors:** Raise with `frappe.throw(_("message"), [ExcClass], title=_("..."))`. There are about 181 call sites. Use `frappe.bold()` for emphasis and `get_link_to_form()` for record links in messages.
- **Typed errors:** Define module-level subclasses of `frappe.ValidationError` (e.g. `OverlapError`, `MaximumCapacityError` in `patient_appointment.py`, `OverlapError` in `insurance_payor_contract.py`). Pass them as the second argument to `frappe.throw` so tests can assert on them.
- **Misconfiguration:** Use `frappe.throw(msg, title=_("Missing Configuration"))` with a link to the settings form (`healthcare/healthcare/utils.py`).
- **Non-fatal side effects (SMS, calendar events, notifications):**
  - Wrap them in `try/except`.
  - Log with `frappe.log_error(frappe.get_traceback(), _("Title"))`.
  - Tell the user with `frappe.msgprint(..., indicator="orange")` or `alert=True` instead of failing the transaction.
- **Client side:** Use `frappe.throw(__("..."))` in form scripts only for UX. The authoritative check must also exist server-side.
- When intentionally throwing in patches, add `# nosemgrep` where Semgrep flags it.
