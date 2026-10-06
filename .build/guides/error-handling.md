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
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/utils.py
  - healthcare/public/js/healthcare_practitioner.js
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
---

- **Validation errors:** call `frappe.throw(_("Message"))`. This raises `frappe.ValidationError` and shows a dialog. There are about 180 call sites. Add `title=_("...")` where it helps, for example `title=_("Missing Configuration")` in `utils.py`.
- **Typed errors:** define domain exceptions in the controller module as subclasses of `frappe.ValidationError` (`OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`). Pass the class as the second argument, `frappe.throw(msg, OverlapError)`, so tests can `assertRaises` it.
- **Message formatting:** `_("... {0} ... {1}").format(frappe.bold(x), frappe.bold(y))` highlights record names.
- **Background or best-effort work** (notifications, calendar events, patches): catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)` instead of failing the transaction.
- **Client side:** `frappe.throw(__('...'))` / `frappe.msgprint` in form scripts for input validation.
- Avoid bare `except Exception` unless you log the error. About 31 exist, mostly in logging paths.
