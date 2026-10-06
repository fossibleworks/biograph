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
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
  - healthcare/permissions.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **Validation errors:** raise them with `frappe.throw(_("message {0}").format(frappe.bold(value)), <ExcClass>, title=_("..."))` (181 uses). Frappe turns these into user-facing dialogs and HTTP error responses, so don't build custom error JSON.
- **Typed errors:** subclass `frappe.ValidationError` in the controller module so tests can `assertRaises` them. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`.
- **Missing setup:** throw with `title=_("Missing Configuration")` and say which settings to fill (see `healthcare/healthcare/utils.py`).
- **Non-blocking failures** (notifications, calendar events, patches): catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("<Short Title>"))` so it appears in Error Log. Don't re-raise. Example: Appointment Confirmation Message Not Sent.
- `frappe.msgprint` (38 uses) is for warnings and info that should not abort the transaction. `frappe.show_alert` and `frappe.msgprint` are the client-side equivalents.
- Avoid bare `except Exception` that hides errors. Existing ones (about 31) should log via `frappe.log_error`.
- Patches that must stop a migration use `frappe.throw(message)  # nosemgrep`.
- Permission checks raise through `frappe.throw` (`healthcare/permissions.py`). Business logic and validation belong on the server, as the PR template says.
