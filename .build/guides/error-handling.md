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
  - healthcare/healthcare/doctype/item_insurance_eligibility/item_insurance_eligibility.py
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
---

Follow the Frappe idioms already used in the codebase.

- **Validation errors:** call `frappe.throw(_("Message"))`, which appears about 180 times. When callers or tests need to tell an error apart, pass a typed exception class, e.g. `frappe.throw(_("Patient already has an appointment booked for the same day!"), OverlapError)`.
- **Custom exception types:** subclass `frappe.ValidationError` and declare them at the top of the controller module: `MaximumCapacityError`, `OverlapError`, `CoverageOverlapError`.
- **Non-fatal side effects** (SMS, notifications, calendar events) are wrapped in `try/except Exception`. They log the error and then warn the user without failing the transaction:
  ```python
  except Exception:
      frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))
      frappe.msgprint(_("Appointment Confirmation Message Not Sent"), indicator="orange")
  ```
- **Patches** wrap risky migrations and call `frappe.log_error(title=...)`, so the migration continues instead of aborting.
- **Client side:** use `frappe.throw(__("..."))` or `frappe.msgprint` in form scripts. The portal uses frappe-ui `ErrorMessage`.
- **Avoid:** some existing code uses `print(f"ERROR - ...")` or swallows exceptions with `continue`. Don't copy that in new code; use `frappe.log_error`.
