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
  - healthcare/patches/v15_0/rename_medical_code_standard_and_medical_code.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

## Validation errors

Use `frappe.throw(_("Message {0}").format(value), title=_("..."))`. This is the dominant pattern, with about 180 call sites. Optionally pass a custom exception class.

Domain exceptions subclass `frappe.ValidationError` and live in the controller module. Examples: `OverlapError` and `MaximumCapacityError` in patient_appointment, `CoverageNotFoundError` and `NoActiveContractError` in patient_insurance_coverage, `CoverageOverlapError`.

For configuration gaps, throw with `title=_("Missing Configuration")`, as `healthcare/healthcare/utils.py` does.

## Non-fatal and background failures

Catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)` so it shows up in Error Log. Examples are the appointment confirmation message and the calendar event creation in patient_appointment.

Patches wrap risky renames in `try/except`. They re-raise unless the error is the expected one, e.g. `if e.args[0] != 1054: raise`.

## Messages

- `frappe.msgprint(_(...))` gives non-blocking user feedback (about 38 uses).
- In Desk JS, use `frappe.throw(__("..."))`, `frappe.msgprint`, or `frappe.show_alert`.

## Avoid

- Bare `except Exception: pass`. One exists in `recuring_appointment_handler.py`; do not copy it.
- `print()` for errors, as at `patient_appointment.py:351`.
- Unwrapped strings.
