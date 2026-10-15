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
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

This code follows standard Frappe idioms.

**Validation and user errors:** use `frappe.throw(_("message {0}").format(...), [ExcClass], title=_("..."))`. There are about 181 calls. `frappe.throw` aborts the request, rolls back the transaction and shows a dialog in the desk or portal.
- Pass `title=` for context, e.g. `title=_("Invalid Healthcare Service Unit")`.
- Use `get_link_to_form(doctype, name)` in messages so users can jump to the conflicting record.

**Typed errors:** declare a module-level subclass of `frappe.ValidationError` when callers or tests need to tell one failure apart, e.g. `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`. Raise it with `frappe.throw(msg, OverlapError)` and test it with `assertRaises(OverlapError)`.

**Non-blocking warnings:** use `frappe.msgprint(...)` (about 38 uses) to inform without aborting.

**Background and side-effect failures:** in scheduler jobs, notifications, calendar sync, billing jobs and patches, wrap in `try/except` and record with `frappe.log_error(...)` so the main flow continues:
- `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`
- `frappe.log_error(message=e, title="Can't bill Service Unit occupancy")`

These entries show up in the desk **Error Log**. Do not swallow exceptions silently, and do not use `print`.

**Validate on the server.** The PR template says "All business logic and validations must be on the server-side". Client JS may pre-check, using `frappe.msgprint` / `frappe.throw` in the browser, but the controller must enforce the rule as well.

**Whitelisted API:** `@frappe.whitelist()` functions raise through `frappe.throw` too. Frappe turns that into the HTTP error response, and frappe-ui `createResource` surfaces it via `onError`. Check permissions (`frappe.has_permission` / `has_website_permission` hooks) before returning patient data.
