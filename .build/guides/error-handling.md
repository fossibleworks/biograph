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
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **Validation errors:** raise them with `frappe.throw(_("Message"))` (about 180 call sites). Frappe turns these into a user-visible dialog and an HTTP error, and rolls back the transaction.
- **Typed errors:** subclass `frappe.ValidationError` per domain condition, defined at the top of the controller module (`OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`, `CoverageOverlapError`), and pass them as the second argument: `frappe.throw(_("..."), OverlapError)`. Tests assert on these classes.
- **Non-blocking notices:** use `frappe.msgprint(_("..."))`.
- **Background/integration failures** (scheduler jobs, notifications, billing side effects, calendar events) are caught and recorded with `frappe.log_error(message/traceback, title)`, so one bad record doesn't abort the batch. Example: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- **Client side:** desk JS uses `frappe.throw(__("..."))` / `frappe.msgprint` for form validation. The portal shows server errors with `toast.error(err.messages?.[0] || err)`.
- Validation belongs on the server (PR template). Client checks are only for UX.
