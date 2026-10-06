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
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/public/js/mark_unavailable.js
---

**User-facing validation errors:** raise them with `frappe.throw(_("Message"), <ExcClass>, title=_("Title"))` (181 call sites). Frappe turns these into a desk message dialog and an HTTP error response, so no custom API error envelope is needed.
- For distinguishable failures, define module-level subclasses of `frappe.ValidationError`, for example `OverlapError` and `MaximumCapacityError` in `patient_appointment.py`, and `OverlapError` in `insurance_payor_contract.py`. Pass the class as the second argument to `frappe.throw`, and catch or assert on it in tests.
- Messages are translatable and use `{0}` placeholders: `_("...{0}").format(frappe.bold(value))`.

**Non-fatal or background failures:** catch the exception and record it with `frappe.log_error(...)` (15 sites). The usual form is `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(title=...)`. This creates an Error Log record instead of interrupting the user. Notifications, calendar-event sync and patches use this pattern.

**Patches:** wrap risky steps in `try/except`, then log with `frappe.log_error` and/or `frappe.logger().error(...)`. The original exception is not re-raised unless the migration must stop.

**Desk JS:** use `frappe.msgprint({...})` for blocking messages and `frappe.show_alert({...})` for toasts. In the portal, use frappe-ui `toast` and `ErrorMessage`, for example "Failed to load appointments".

Keep validation in the controller's `validate`/`before_submit` hooks on the server. Client-side checks are only a convenience.
