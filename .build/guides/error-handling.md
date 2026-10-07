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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/public/js/sales_invoice.js
  - patient_portal/src/components/Payment.vue
---

- **Validation errors:** raise them with `frappe.throw(_("Message"), ExcClass, title=_("Title"))`. There are about 181 call sites. Domain exceptions subclass `frappe.ValidationError` and are named `<Something>Error`, for example `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError` and `NoActiveContractError`. Define them at the top of the doctype controller so tests can `assertRaises` them.
- **Missing setup:** messages link to the settings form with `get_link_to_form("Healthcare Settings", ...)` and use `title=_("Missing Configuration")`.
- **Background or best-effort work** (calendar events, patches): catch `Exception` and record it with `frappe.log_error(message_or_traceback, "<Short Title>")` so it lands in the Error Log doctype instead of interrupting the user. Use this sparingly; there are about 31 `except Exception` sites.
- **Desk JS:** show problems with `frappe.msgprint(__("..."))` and quick confirmations with `frappe.show_alert({message, indicator})`.
- **Patient Portal:** show errors with frappe-ui `ErrorMessage` / `Dialog` components.
- Avoid `print()` debugging in controllers. Some existing code, such as `patient_appointment.py`, still has `print("DEBUG ...")`. Do not copy that pattern.
