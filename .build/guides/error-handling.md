---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/utils.py
  - healthcare/setup.py
  - patient_portal/src/components/Payment.vue
---

- **User-facing validation:** `frappe.throw(_("Message {0}").format(x), title=_("Title"))` aborts the request and rolls back. There are about 181 uses. Pass a specific exception class when callers or tests need it.
- **Custom exceptions** subclass `frappe.ValidationError`, for example `MaximumCapacityError` and `OverlapError` in `patient_appointment.py`. Pass them as the second argument: `frappe.throw(msg, OverlapError)`.
- **Non-fatal notices** use `frappe.msgprint` (about 38 uses). Desk JS uses `frappe.throw(__())`, `frappe.confirm`, and `frappe.show_alert`.
- **Background or side-effect failures** (notifications, calendar events, patches) are caught with `except Exception` and recorded with `frappe.log_error(frappe.get_traceback(), _("Title"))` so the main transaction still completes.
- Expected duplicates in setup code are caught specifically (`except frappe.DuplicateEntryError`).
- The Vue portal shows API errors with frappe-ui's `<ErrorMessage :message="error" />`.
