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
  - healthcare/regional/india/abdm/utils.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Validation and user errors:** use `frappe.throw` (about 181 call sites). It raises `frappe.ValidationError` (or a subclass) and shows the message to the user.
```python
frappe.throw(_("Appointment end must be after start."))
frappe.throw(msg, title=_("Missing Configuration"))
frappe.throw(_("Patient already has an appointment booked for the same day!"), OverlapError)
```
- Always translate messages with `_()`. Pass a `title=` for configuration problems. When the fix is a settings change, link to it with `get_link_to_form("Healthcare Settings", "Healthcare Settings")`.
- Define domain-specific exception classes, such as `OverlapError` in patient_appointment, when callers or tests need to catch them.
- Business rules and validation belong on the **server**, in controller `validate`/`before_submit` methods. The PR template says so explicitly.
- Use `frappe.msgprint` for non-blocking warnings.

**Background and integration failures:** catch the exception, log it with `frappe.log_error(frappe.get_traceback(), _("<Short Title>"))` (about 15 call sites), and carry on when the failure must not block the main transaction. Examples are notifications (`Appointment Confirmation Message Not Sent`), calendar events and patches.

**External HTTP (ABDM):** call `response.raise_for_status()` inside `try`, record each request/response in an `ABDM Request` doc for auditing, and handle `json.decoder.JSONDecodeError` separately.

**Client-side:** use `frappe.msgprint(__("..."))` / `frappe.throw` in form scripts for guard conditions. The server's thrown messages reach the UI automatically through `frappe.call`.

**Avoid:** `print(...)`-based error output. `patient_appointment.py` contains `print(f"ERROR - ...")` / `DEBUG` prints, which is legacy and should not be copied. Also avoid bare `except Exception` that swallows the error without `log_error`.
