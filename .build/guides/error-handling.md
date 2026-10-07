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
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/patches/v15_0/rename_medical_code_standard_and_medical_code.py
---

- **Validation errors go to users through `frappe.throw(_("..."), title=_("..."))`** (about 180 call sites). Pass an error class when the caller or tests need to distinguish the case.
- **Custom exceptions** subclass `frappe.ValidationError` and are defined at the top of the controller module:
  - `OverlapError`, `MaximumCapacityError` (patient_appointment)
  - `CoverageNotFoundError`, `NoActiveContractError` (patient_insurance_coverage)
  - `CoverageOverlapError`
- Frappe's built-ins are also used: `frappe.PermissionError`, `DuplicateEntryError`, `MandatoryError`, `DoesNotExistError`.
- **Non-blocking notices** use `frappe.msgprint(_(...))`.
- **Background or best-effort failures** are caught and recorded with `frappe.log_error(...)` (Error Log DocType) instead of breaking the user transaction. Examples: notification sending, calendar event cleanup, sample collection, payment records, patch loops.
  - Include a descriptive title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- **Patches:** wrap per-record work in `try/except Exception` and call `log_error` so one bad row doesn't abort the migration. Re-raise unexpected DB error codes (e.g. check `e.args[0] != 1054`).
- Avoid bare `except Exception` in request paths unless you log the error. `# nosemgrep` is used sparingly where `frappe.throw` in patches is intentional.
