---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/doctype/clinical_procedure/clinical_procedure.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/doctype/inpatient_medication_entry/inpatient_medication_entry.py
  - healthcare/healthcare/doctype/patient/patient.js
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

## Validation errors go to the user through `frappe.throw`

- Server-side validation is the norm. The PR template says "All business logic and validations must be on the server-side". The codebase has about 180 `frappe.throw` calls.
- Always translate messages and use a title where it helps: `frappe.throw(_("Price List is mandatory"), title=_("Price List Not Set"))`. Pass an exception class to get the right HTTP status, e.g. `frappe.throw(_("Not allowed to print this document."), frappe.PermissionError)`.
- For domain-specific failures, define a subclass of **`frappe.ValidationError`** in the DocType module and raise it via `frappe.throw(msg, OverlapError)`. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`. Tests can then `assertRaises` the specific class.
- Long or tabular errors may use `is_minimizable=True, wide=True` (see inpatient medication entry).

## Background and non-critical failures are logged, not raised

- In scheduler jobs, notifications, patches and integrations, catch the exception and record it with **`frappe.log_error`**, giving a title (`frappe.log_error(message=e, title="Can't bill Service Unit occupancy")`, `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`). This keeps one bad record from aborting a whole batch.
- Avoid bare `except Exception:` that swallows errors silently. If you catch, log with a descriptive title.

## Client side

- Desk JS uses `frappe.throw(__("..."))` to block an action and `frappe.msgprint(__("..."))` for information.
- Whitelisted portal APIs return `None` or empty results for "not found" cases (e.g. `get_logged_in_patient`) and throw for permission violations.
