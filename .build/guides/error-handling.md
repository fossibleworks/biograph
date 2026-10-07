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
  - healthcare/healthcare/doctype/item_insurance_eligibility/item_insurance_eligibility.py
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **Validation failures** raise through `frappe.throw(_("…"))`. There are about 180 call sites in Python.
  - Pass a typed exception as the second argument when callers or tests need to catch it, for example `frappe.throw(msg, OverlapError)`.
  - Pass a `title=_("Missing Configuration")` for configuration problems.
  - Highlight record names with `frappe.bold(...)`.
- **Custom exceptions** are module-level classes subclassing `frappe.ValidationError`: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`. They are defined at the top of the controller that raises them.
- **Business rules belong on the server.** The PR template says: "All business logic and validations must be on the server-side". Put them in `validate` and the other controller hooks. JS `frappe.throw` and `frappe.msgprint` are for client-side UX guards only.
- **Non-blocking information** goes through `frappe.msgprint(_("…"))`.
- **Background and non-critical failures**, such as notifications, calendar events and patches, are caught and recorded with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)` so the main transaction is not aborted. An example is "Appointment Confirmation Message Not Sent".
- Use broad `except Exception` mostly in patches and uninstall code. In controllers, let `frappe.throw` propagate so Frappe rolls back the request and shows the message.
