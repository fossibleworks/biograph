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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
---

**Validation errors**
- Use `frappe.throw(_("Message"), [ExceptionClass], title=_("..."))`. There are about 180 uses in Python.
- Messages are translatable and use `{0}` placeholders with `.format(...)`. Examples: `_("User {0} is disabled")`, `_("{0} is a holiday")`.
- Missing setup uses a title such as `title=_("Missing Configuration")`.

**Typed errors**
- Domain-specific exceptions subclass `frappe.ValidationError` and are defined at module level in the controller. Examples:
  - `OverlapError`, `MaximumCapacityError` (Patient Appointment);
  - `CoverageOverlapError`;
  - `CoverageNotFoundError`, `NoActiveContractError` (Patient Insurance Coverage).
- Pass them as the second argument: `frappe.throw(msg, OverlapError)`.
- Tests assert with `self.assertRaises(OverlapError, ...)`.

**Non-blocking warnings**
- `frappe.msgprint(...)`, about 40 uses.

**Background and side-effect failures**
- For notifications, calendar events and patches, catch the exception and call `frappe.log_error(frappe.get_traceback(), _("Title"))` (or `frappe.log_error(title=...)`) so the main transaction still completes.
- Examples are the appointment confirmation message and the unavailability calendar event.

**Client side**
- `frappe.throw(__("..."))` in form scripts (about 40 uses), plus `frappe.confirm` for destructive actions.
- Validation must also be enforced on the server.

**What not to do**
- `ruff` ignores B904, so `raise ... from` is not enforced. Still avoid bare `except:` that swallows errors.
- Do not leave `print()` in non-test code. The pre-commit `debug-statements` hook catches debugger calls.
