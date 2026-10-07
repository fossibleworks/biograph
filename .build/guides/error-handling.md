---
title: Error handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/healthcare_settings/healthcare_settings.py
---

- **Validation errors:** raise them with `frappe.throw(_("Message").format(...), title=_("..."))`, which has about 181 call sites. Pass a typed exception as the second argument when callers need to catch it (e.g. `frappe.throw(msg, OverlapError)`).
- **Domain exception classes** subclass `frappe.ValidationError`: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`.
- **Permission failures:** `frappe.throw(_("Not allowed ..."), frappe.PermissionError)`. This pattern appears in the portal API.
- **Missing configuration:** throw with `title=_("Missing Configuration")` and include a `get_link_to_form("Healthcare Settings", ...)` link so the user can fix it.
- **Background or non-fatal failures:** catch the exception and call `frappe.log_error(message_or_traceback, title)` rather than failing the transaction. This is used in patches and in unavailability calendar events. Avoid broad `except Exception` without logging.
- **Non-blocking info:** use `frappe.msgprint`. In JS, use `frappe.show_alert` for transient notices, `frappe.msgprint` for dialogs, and `frappe.throw(__())` for client-side validation.
- Frappe turns thrown exceptions into the standard API error response. Do not build custom JSON error envelopes in whitelisted methods.
