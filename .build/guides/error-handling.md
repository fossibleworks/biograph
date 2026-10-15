---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
---

## Validation and user errors

Raise user and validation errors with **`frappe.throw(_("..."), <ExcType>, title=_("..."))`**. This is the dominant pattern, with about 180 uses.

- The message is translatable and uses `{0}` placeholders with `.format(...)`.
- Add a specific exception class where callers or tests need one, for example `frappe.PermissionError` ("Not allowed to print this document."), `frappe.DoesNotExistError` or `frappe.MandatoryError`.
- Define domain exceptions as subclasses of `frappe.ValidationError` near the controller: `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`.
- Use `title=` for grouped messages (e.g. `title=_("Missing Configuration")` in `utils.py`).

## Non-fatal messages

Use `frappe.msgprint(_(...))` for informational or non-blocking feedback.

## Background and side-effect failures

Inside `try/except` around non-critical side effects (notifications, calendar events, billing of occupancy), log with **`frappe.log_error(...)`** and do not re-raise. This writes an Error Log doc. Example:

```python
frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))
```

## Client side

Desk JS uses `frappe.throw(__("..."))` and `frappe.msgprint`. Whitelisted APIs return plain data or `None` rather than error envelopes; exceptions become standard Frappe HTTP error responses.

## Rule

Keep validations server-side in `validate()`/`before_submit()` so that API and import paths are protected too.
