---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

- **User-facing validation:** raise with `frappe.throw(_("message {0}").format(x))`, optionally adding `title=_(...)` or an exception class (e.g. `frappe.throw(..., frappe.PermissionError)`). There are about 180 call sites. Validations belong in the controller's `validate`/`before_submit`, server-side.
- **Domain exceptions** subclass `frappe.ValidationError` at module top. Examples: `OverlapError` and `MaximumCapacityError` in patient_appointment, and `CoverageNotFoundError` and `NoActiveContractError` in patient_insurance_coverage. Tests can then `assertRaises` on them.
- **Configuration gaps:** use `frappe.throw(msg, title=_("Missing Configuration"))`, often with `get_link_to_form` in the message (see `healthcare/healthcare/utils.py`).
- **Non-fatal / background failures** (SMS, calendar events, history updates) are caught with `try/except` and recorded with `frappe.log_error(...)`. Pass a title, and use `frappe.get_traceback()` where available, so the main transaction is not blocked.
- **Informational notices** use `frappe.msgprint`.
- **Desk JS** uses `frappe.throw(__(...))` for blocking errors, `frappe.msgprint` for info, `frappe.show_alert` for transient feedback and `frappe.confirm` before destructive actions.
- **Permissions:** whitelisted APIs check access explicitly and throw `frappe.PermissionError` (e.g. the portal print check).
