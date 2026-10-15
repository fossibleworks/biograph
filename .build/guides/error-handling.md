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
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/lab_test/lab_test.js
  - healthcare/www/patient_portal.py
---

# Error handling

## Validation errors (user-facing)
- Raise with `frappe.throw(_("Message {0}").format(value))` (about 181 call sites). Frappe aborts the transaction and shows a dialog.
- For errors callers or tests need to tell apart, subclass `frappe.ValidationError` in the DocType module and pass it as the second argument:
  ```python
  class OverlapError(frappe.ValidationError):
  	pass

  frappe.throw(_("Patient already has an appointment booked for the same day!"), OverlapError)
  ```
  Existing classes: `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`, `CoverageOverlapError`.
- Validate on the server in controller hooks (`validate`, `before_submit`). Desk JS checks are only for UX.

## Non-fatal / background failures
- When a side effect (notifications, calendar events, billing of occupancy, patches) must not block the main flow, wrap it in `try/except` and record it with `frappe.log_error(...)`. Pass a title, usually `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(message=e, title="...")`. These land in the Error Log doctype.
- Do not silently swallow exceptions without `log_error`.

## Client side
- Desk JS reports problems with `frappe.msgprint(__("..."))` and confirms success with `frappe.show_alert({message: __("..."), indicator: "green"})`.
- Whitelisted API methods raise via `frappe.throw`. The portal relies on frappe-ui resources to surface `exc` messages.
- Guard dev-only endpoints with checks like `if not frappe.conf.developer_mode: frappe.throw(...)`.
