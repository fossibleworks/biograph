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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/setup.py
  - healthcare/public/js/sales_invoice.js
---

- **Validation errors:** use `frappe.throw(_("message"), ExcClass, title=_(...))`. This is the dominant pattern, with about 180 call sites. Messages are translatable and use `.format()` placeholders with `frappe.bold(...)` for emphasis.
- **Typed errors:** each doctype defines its own `frappe.ValidationError` subclasses (`OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`) and passes them as the second argument to `frappe.throw` so tests can `assertRaises` them.
- **Configuration gaps:** throw with `title=_("Missing Configuration")` (see `healthcare/healthcare/utils.py`).
- **Non-fatal side effects** (notifications, calendar events, patches): wrap them in `try/except Exception` and record with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)`. This keeps the main transaction going. Catch specific Frappe exceptions such as `frappe.DuplicateEntryError` where you know them (see `healthcare/setup.py`).
- **Client side:** `frappe.msgprint(__(...))` for blocking messages and `frappe.show_alert` for transient ones.
- Do not swallow errors silently. Every broad `except` should log through `frappe.log_error`.
