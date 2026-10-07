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
  - healthcare/public/js/sales_invoice.js
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
---

- **User and validation errors:** raise them with `frappe.throw(_("Message {0}").format(x), [ExcClass], title=_("Title"))` (about 181 call sites). Titles such as `_("Missing Configuration")` and `_("Not Available")` group errors of the same kind.
- **Typed errors:** subclass `frappe.ValidationError` at module level, for example `OverlapError` and `MaximumCapacityError` in `patient_appointment.py` and `OverlapError` in `insurance_payor_contract.py`. Pass the class to `frappe.throw(..., OverlapError)` so tests can `assertRaises` it.
- **Background and best-effort work** (notifications, calendar events, patches): catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)`. This writes to the Error Log doctype. Do not let it break the main transaction. An example is "Appointment Confirmation Message Not Sent".
- In Desk JS, use `frappe.throw(__("..."))` for client-side guards and `frappe.msgprint` for notices.
- Whitelisted portal APIs check permissions and patient ownership through `has_website_permission` hooks and helpers such as `get_patients_with_relations()`. If nothing applies they return early (`return`) instead of raising.
- Version-compatibility patches use `frappe.throw(message)  # nosemgrep`. Add a semgrep suppression only where it is deliberate.
