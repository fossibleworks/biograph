---
title: Error Handling
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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - patient_portal/src/components/Payment.vue
---

- **Validation errors go to the user through `frappe.throw`** (about 180 uses). Wrap the message in `_()`, and pass a `title=` when that helps, e.g. `frappe.throw(msg, title=_("Missing Configuration"))`. Pass an exception class when callers or tests need to distinguish it, e.g. `frappe.throw(_("Not allowed to print this document."), frappe.PermissionError)`.
- **Domain exception classes** subclass `frappe.ValidationError` and are declared at the top of the controller module: `OverlapError`, `MaximumCapacityError` (patient_appointment), `CoverageNotFoundError`, `NoActiveContractError` (patient_insurance_coverage), `CoverageOverlapError`.
- **Non-blocking notices** use `frappe.msgprint` (about 38 uses).
- **Background and scheduler jobs:** catch `Exception`, record it with `frappe.log_error(title=..., message=frappe.get_traceback())`, then either continue with the next record (see `medication_request.update_expired_medication_requests`) or re-raise when the caller must fail (`inpatient_record`: `log_error` then `raise`).
- **Whitelisted APIs:** check permissions and existence explicitly and throw `frappe.PermissionError` or `frappe.DoesNotExistError`. Returning `None` for "not found" is also used in portal APIs (`get_logged_in_patient`).
- **Client side:** desk JS validates input with `frappe.throw(__('...'))`. Portal Vue components show errors with frappe-ui `<ErrorMessage :message="error" />`.
- **Avoid:**
  - bare `print(...)` for errors (some legacy code in `patient_appointment.py` does this)
  - `except Exception: continue` with no logging
  - swallowing errors inside `validate`
