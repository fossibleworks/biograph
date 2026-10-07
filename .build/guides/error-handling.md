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
  - healthcare/setup.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/public/js/sales_invoice.js
---

## User-facing validation

- Raise with `frappe.throw(_("message {0}").format(...))` (about 181 call sites). Add `title=_("Missing Configuration")` for settings problems. Pass a specific exception class when callers need to catch it, for example `frappe.throw(..., OverlapError)` in Patient Appointment.
- Use `frappe.bold(value)` to highlight field values in messages.
- Validate in controller hooks (`validate`, `before_submit`, …) on the server, not only in JS.

## Catching

- Catch specific Frappe exceptions where you can, for example `except frappe.DuplicateEntryError:` in `setup.py`.
- Use broad `except Exception` only in patches, setup and background jobs. In those cases, record the failure with `frappe.log_error(frappe.get_traceback(), _("<Title>"))` (or `frappe.log_error(title=...)`) and keep going. Do not swallow errors silently. Notification side effects work this way, for example "Appointment Confirmation Message Not Sent".
- Patches that must abort use `frappe.throw(message)  # nosemgrep`.

## Client side

Desk JS reports problems with `frappe.msgprint(__("..."))` or `frappe.throw`. Server errors raised by `frappe.throw` surface automatically to both desk and portal (frappe-ui resources).
