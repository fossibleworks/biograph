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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/public/js/sales_invoice.js
---

**Validation errors (user-facing):** use `frappe.throw(_("Message"))`. This raises `frappe.ValidationError` and rolls back the transaction. There are about 180 call sites.
- When callers or tests need to tell a failure apart, define a module-level subclass of `frappe.ValidationError` in the DocType controller and pass it as the second argument:
  ```python
  class OverlapError(frappe.ValidationError):
  	pass
  frappe.throw(_("Patient already has an appointment booked for the same day!"), OverlapError)
  ```
  Existing examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`.
- Use `frappe.throw(msg, title=...)` for multi-line messages. Interpolate with `_("...{0}").format(frappe.bold(x))`-style formatting.

**Non-fatal side effects** (messaging, calendar events, realtime): wrap them in `try/except Exception` so the main transaction still succeeds. Record the failure with `frappe.log_error(...)`, which creates an Error Log document. Notify the user with `frappe.msgprint(_(...), indicator="orange")` where needed:
```python
try:
	send_message(doc, message)
except Exception:
	frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))
	frappe.msgprint(_("Appointment Confirmation Message Not Sent"), indicator="orange")
```

**Patches:** per-record `try/except` with `frappe.log_error(..., "<Patch Name>")`, so one bad row does not abort a migration.

**Client side:** form scripts use `frappe.throw(__("..."))` and `frappe.msgprint(__("..."))` for validation in dialogs.

**Avoid** in new code: `print()` for errors, which exists once in `patient_appointment.py`, and bare `except Exception` that swallows errors without logging. Ruff's B904 (raise-from) is disabled, so the codebase does not chain exceptions.
