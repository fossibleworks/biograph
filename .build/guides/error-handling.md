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
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
---

- **Validation errors:** raise them with `frappe.throw(_("Message"))` (about 180 call sites). Interpolate with `.format()` and `{0}` placeholders, and wrap identifiers in `frappe.bold()`. Avoid f-strings inside `_()`: some exist, but they break translation.
- **Typed errors:** define a subclass of `frappe.ValidationError` in the controller module and pass it as the second argument to `frappe.throw`. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`. Tests can then use `assertRaises(OverlapError)`.
- **Non-blocking warnings:** `frappe.msgprint(_(...), indicator="orange")`.
- **Side-effects that may fail** (notifications, calendar events, patches): wrap them in `try/except Exception`, record with `frappe.log_error(frappe.get_traceback(), _("Title"))` (traceback or message first, title second) and continue. Example: `Appointment Confirmation Message Not Sent`.
- **Do not** use `print()` for errors. One legacy instance exists in `patient_appointment.py`; do not copy it.
- **Client side:** `frappe.msgprint(__("..."))` in form scripts; the portal uses frappe-ui `ErrorMessage`.
- **Patches:** idempotent, guarded with try/except and `frappe.log_error` so a migration does not abort on one bad row.
