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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/public/js/sales_invoice.js
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **Validation errors (server):** raise them with `frappe.throw(_("Message {0}").format(val), title=_("Title"))`. Pass an exception class when callers or tests need to tell errors apart, e.g. `frappe.throw(msg, OverlapError)` or `frappe.throw(_(msg), frappe.ValidationError)`. Domain exceptions subclass `frappe.ValidationError` and are declared at the top of the controller (`MaximumCapacityError`, `OverlapError` in `patient_appointment.py` and `insurance_payor_contract.py`). Use `title=_("Missing Configuration")` for missing settings (`healthcare/healthcare/utils.py`).
- Validation belongs in controller hooks (`validate`, `before_submit`, `on_submit`, …) or in `doc_events` functions wired in `hooks.py`. The PR template states that all validations must be server-side.
- **Background or best-effort failures** (notifications, calendar events, scheduler jobs) should not block the user. Catch them and record them in the Error Log with `frappe.log_error(...)`: pass `frappe.get_traceback()` or a message plus a descriptive title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- Broad `except Exception` exists in about 31 places, mostly around messaging and integrations. When catching broadly, always log. Never swallow silently.
- **Client side:** use `frappe.throw(__("..."))` for blocking validation in form scripts, `frappe.msgprint(__("..."))` for informational dialogs, and `frappe.show_alert({...})` for toasts.
- Patches that must abort use `frappe.throw(message)  # nosemgrep` (the version-compatibility checks).
- Ruff B904 (raise without `from`) is ignored, so re-raising with context is optional. B017 is ignored for `assertRaises(Exception)`, but specific exception classes are preferred.
