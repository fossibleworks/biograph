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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/healthcare/doctype/insurance_payor/insurance_payor.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - patient_portal/src/components/BookAppointmentModel.vue
---

## Validation and user errors
- Raise them with `frappe.throw(_("..."), title=_("..."))`. There are about 181 uses.
- Use positional placeholders through `.format()`, for example `_("Patient {0} is not admitted in the service unit {1}").format(...)`.
- Pass a `title` for configuration problems, for example `title=_("Missing Configuration")` in `healthcare/healthcare/utils.py`.

## Typed errors
- Define domain exceptions as subclasses of `frappe.ValidationError` at module level, for example `MaximumCapacityError` and `OverlapError` in `patient_appointment.py` and `insurance_payor_contract.py`.
- Pass them as `frappe.throw(msg, OverlapError)` so tests can `assertRaises` them.

## Non-fatal notices
- Use `frappe.msgprint(_(...), alert=True)` for success or info toasts, for example "Customer {0} is created."

## Background and best-effort failures
- Catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(title=...)`. This shows up in Error Log. There are about 15 uses, for example "Appointment Confirmation Message Not Sent".
- Do not re-raise when the failure must not block the main transaction, such as notifications and calendar events.
- `except Exception` appears about 31 times. Keep it limited to these best-effort paths.

## API endpoints
- Whitelisted endpoints in `api/patient_portal.py` return plain data or `None` and rely on `frappe.throw` for errors.
- The portal shows errors with frappe-ui `toast.error(err.messages?.[0] || err)`.

## Patches
- Patches log failures with `frappe.log_error` or `frappe.logger().error` rather than aborting the migration, unless there is a hard version-compatibility check. Those checks use `frappe.throw` with `# nosemgrep`.
