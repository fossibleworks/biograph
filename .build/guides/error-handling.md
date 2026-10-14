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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/public/js/sales_invoice.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

# Error handling

## Validation errors (the main pattern)
- Raise user-facing errors with **`frappe.throw(_("Message {0}").format(value), title=_("..."))`** (≈180 call sites). Frappe turns these into a dialog in Desk and an error response for API calls.
- For errors other code needs to catch, subclass `frappe.ValidationError` in the controller module, then raise with `frappe.throw(msg, exc=OverlapError)`. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`.
- Use `title=_("Missing Configuration")` for settings that haven't been configured.
- `# nosemgrep` is used where semgrep flags a throw with a non-literal message.

## Non-fatal failures
- Background or side-effect failures (SMS, calendar events, notifications, setup routines) are caught, logged with **`frappe.log_error(...)`**, and reported to the user without blocking: `frappe.msgprint(_("..."), indicator="orange")` or `alert=True`. Example: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- Prefer `frappe.log_error(title=..., message=...)` so the error shows up in the Error Log doctype.

## Client side
- Desk JS shows errors with `frappe.msgprint(__("..."))` or `frappe.show_alert({...})`.
- The portal uses frappe-ui's `ErrorMessage` component.
- Validation must still be enforced on the server (PR template rule).
