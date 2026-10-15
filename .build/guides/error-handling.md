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
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - patient_portal/src/components/Payment.vue
---

- **User-facing validation:** `frappe.throw(_("Message {0}").format(...), title=_("..."))` (~180 uses). It raises a `ValidationError` that aborts the transaction and shows a dialog. Put validation in controller `validate*` methods on the server.
- **Typed errors:** subclass `frappe.ValidationError` at the top of the controller module and pass it with `frappe.throw(msg, exc=OverlapError)` (e.g. `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`). Tests assert on these types.
- **Missing configuration:** throw with `title=_("Missing Configuration")` and include a link built with `get_link_to_form` (pattern in `healthcare/healthcare/utils.py`).
- **Non-blocking info:** `frappe.msgprint(_(...))` for confirmations such as "Customer {0} created and linked to Patient".
- **Background/side-effect failures** (SMS, calendar events, scheduled billing): wrap in `try/except Exception` and record with `frappe.log_error(message/traceback, title)` so the main flow continues (e.g. inpatient occupancy billing, appointment confirmation messages).
- **Desk JS:** `frappe.throw(__(...))` / `frappe.msgprint(__(...))` in form scripts. **Portal:** surface errors with frappe-ui `<ErrorMessage :message="error" />`.
