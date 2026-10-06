---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
---

- **Validation errors:** raise them with `frappe.throw(_("message"), [ExcClass], title=_("Title"))`. There are about 180 uses. Messages are translated with `_()` and use `{0}` placeholders. Links to config records are built with `get_link_to_form(...)`, e.g. `frappe.throw(msg, title=_("Missing Configuration"))`.
- **Typed errors:** domain-specific exceptions subclass `frappe.ValidationError` inside the controller module: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`. Pass the class as the second argument to `frappe.throw` so tests can `assertRaises` on it.
- **Non-fatal user notices:** `frappe.msgprint` on the server, and `frappe.show_alert({message, indicator})` / `frappe.msgprint` on the client.
- **Background or best-effort failures** (notifications, calendar events, patches): catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(title=...)`. This logs to the Error Log doctype and does not break the user flow. Example: "Appointment Confirmation Message Not Sent".
- Broad `except Exception` is used about 31 times, mainly in patches and integrations. Prefer narrow catches in new code.
- Use server-side validation in controller `validate()` / `before_submit()` hooks, not client-only checks (PR template).
