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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
---

- **Validation errors:** raise them with `frappe.throw(_("Message"), OptionalExceptionClass)` (about 180 uses). For conditions callers may need to tell apart, define module-level subclasses of `frappe.ValidationError`, e.g. `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`.
- Format messages with `_()` and `.format()`, and link records with `frappe.bold` or `get_link_to_form`.
- **Non-blocking notices:** use `frappe.msgprint(_(...))`.
- **Background or best-effort failures** (notifications, calendar events, patches): catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)`, so the main transaction is not blocked.
- Avoid bare `except Exception` without logging. Where it already exists, it is paired with `log_error`.
- **Desk JS:** use `frappe.throw`/`frappe.msgprint` and `frappe.confirm` for confirmations.
