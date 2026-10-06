---
title: Error handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/permissions.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/practitioner_availability/test_practitioner_availability.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
  - healthcare/public/js/sales_invoice.js
---

## User and validation errors (server)
- Raise errors with **`frappe.throw(_("…"))`**. Add a `title=` for grouped error kinds, e.g. `title=_("Missing Configuration")`. Where a setting is missing, include a link to the form with `get_link_to_form("Healthcare Settings", "Healthcare Settings")`.
- Pass a specific exception class when callers or tests need to tell errors apart, e.g. `frappe.PermissionError` in `healthcare/permissions.py` or `frappe.ValidationError`. Domain errors subclass `frappe.ValidationError`, for example `MaximumCapacityError` and `OverlapError` in `patient_appointment.py` and `OverlapError` in `insurance_payor_contract.py`. Tests assert them with `assertRaises(frappe.ValidationError)`.
- Run validations in controller hooks (`validate`, `before_submit`, …) or in `doc_events`. Do not rely on client-side checks; the PR template requires server-side validation.

## Background and best-effort failures
- Non-fatal failures in schedulers, notifications and patches are caught and recorded with **`frappe.log_error(...)`** (Error Log doctype). Pass a title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`. Do not swallow these errors silently.
- Version-compatibility patches use `frappe.throw(message)  # nosemgrep` to abort migration.

## Client (desk JS)
- Use `frappe.throw(__("…"))` to block an action, `frappe.msgprint(__("…"))` to inform, and `frappe.show_alert({...})` for transient success notices.
