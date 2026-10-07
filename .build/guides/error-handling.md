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
  - healthcare/healthcare/doctype/lab_test/lab_test.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/permissions.py
---

- **Validation errors:** raise them with `frappe.throw(_('message'), ExcClass, title=_('...'))` (about 180 uses). Messages are translatable and use `.format()` with `frappe.bold(...)` around values. Example: `frappe.throw(_('Patient already has an appointment booked for the same day!'), OverlapError)`.
- **Custom exception types:** define them at module level as subclasses of `frappe.ValidationError`, named `<Thing>Error`. Examples: `OverlapError` and `MaximumCapacityError` in `patient_appointment.py`, `CoverageOverlapError`, `CoverageNotFoundError` and `NoActiveContractError` in the insurance doctypes. Callers and tests use these types to catch specific errors.
- **Non-blocking warnings:** use `frappe.msgprint(...)`.
- **Missing setup:** use a consistent title such as `title=_('Missing Configuration')` (see `healthcare/utils.py`).
- **Background or non-fatal failures:** catch the exception and record it with `frappe.log_error(message_or_traceback, title)` instead of failing the user action. Example: `'Unavailability Calendar Event Error'` in `patient_appointment.py`.
- **Patches:** wrap risky steps in `try/except` and call `frappe.log_error(frappe.get_traceback(), title)`. Version-gate patches deliberately throw, marked with `# nosemgrep`.
- **Desk JS:** use `frappe.throw` / `frappe.msgprint({title: __('...'), message})` for client-side validation.
- Whitelisted API methods rely on Frappe's standard error responses. They raise with `frappe.throw` and do not return custom error payloads.
