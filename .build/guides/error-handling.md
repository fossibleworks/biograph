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
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
---

- **Validation errors:** use `frappe.throw(_("message"), ExcClass?, title=_("..."))`. There are about 181 call sites. Messages are translated and use `{0}` placeholders with `.format()`, wrapping names in `frappe.bold` where the surrounding code does.
- **Typed errors:** domain exceptions subclass `frappe.ValidationError` and are defined at module top in the doctype controller, e.g. `OverlapError` and `MaximumCapacityError` in `patient_appointment.py`, and `CoverageNotFoundError` and `NoActiveContractError` in `patient_insurance_coverage.py`. Pass them as the second argument to `frappe.throw` so tests can `assertRaises` them.
- **Configuration problems:** throw with `title=_("Missing Configuration")` (see `healthcare/healthcare/utils.py`).
- **Non-blocking failures** (notifications, calendar or conferencing side effects, background jobs): catch the exception, call `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(title=...)`, and carry on. If needed, tell the user with `frappe.msgprint`. Never swallow the exception silently.
- **Patches:** catch broad `Exception` only to re-raise unless the error is the specific expected one (e.g. `if e.args[0] != 1054: raise`), or to log it through `frappe.log_error`.
- **Whitelisted APIs:** return early or empty for no-data cases (e.g. `get_appointments` returns when there are no patients). Use `frappe.throw` / `frappe.PermissionError` for invalid access. Permission hooks live in `healthcare/permissions.py`.
- The bare `except Exception` blocks (about 31) are mostly in patches and uninstall. Avoid adding new ones in controllers.
