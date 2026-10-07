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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/setup.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/public/js/sales_invoice.js
---

- **Validation errors go to the user through `frappe.throw`** (about 180 uses). Use a translated message and, where useful, a `title=_(...)`. Existing titles include "Missing Configuration", "Customer Not Found" and "Invalid Healthcare Service Unit". Link to the misconfigured record with `get_link_to_form("Healthcare Settings", "Healthcare Settings")`.
- **Typed errors:** subclass `frappe.ValidationError` per domain, e.g. `MaximumCapacityError` and `OverlapError` in `patient_appointment.py`. Pass the class as `frappe.throw(msg, OverlapError)` so tests and callers can catch it specifically.
- **Non-blocking notices:** use `frappe.msgprint`.
- **Background or side-effect failures** (notifications, calendar events, patches) are caught and recorded with `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(title=...)` instead of failing the user transaction. Examples include "Appointment Confirmation Message Not Sent" and "Unavailability Calendar Event Error".
- Catch specific Frappe exceptions where possible (`except frappe.DuplicateEntryError:` in setup). Broad `except Exception` is limited to patches and best-effort side effects.
- Desk JS guards with `frappe.throw(__("Please select a Patient to be invoiced"))` before `frappe.call`.
- Whitelisted API functions validate input and permissions server-side (`healthcare/permissions.py` throws on denied access).
