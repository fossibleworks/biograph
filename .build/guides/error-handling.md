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
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient/patient.py
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

- **Validation errors:** raise them with `frappe.throw(_("Message"), ExcClass, title=_("Title"))`. This is the dominant pattern, with about 180 calls. Messages are always translated with `_()` and use `{0}` placeholders with `.format(...)`, often including `frappe.bold(...)` or links to the offending record.
- **Custom exception types** subclass `frappe.ValidationError` and are declared at the top of the controller module, for example `MaximumCapacityError` and `OverlapError` in `patient_appointment.py` and `OverlapError` in `insurance_payor_contract.py`. Tests assert on them with `assertRaises`.
- Use the framework exception classes where they fit: `frappe.PermissionError` for access checks in portal APIs ("Not allowed to print this document.") and `frappe.DuplicateEntryError` for duplicates.
- **Non-blocking notices:** `frappe.msgprint(_(...), alert=True / indicator=...)`.
- **Background or best-effort failures** such as notifications, calendar events, payment records and patches are caught and logged with `frappe.log_error(message/traceback, title)` instead of being raised. Example: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- **Patches** wrap risky renames in `try/except Exception` and log the failure, so a migration does not abort.
- **Desk JS:** use `frappe.throw(__(...))` / `frappe.msgprint` and `frappe.confirm(__("Are you sure ...?"))` before destructive actions.
