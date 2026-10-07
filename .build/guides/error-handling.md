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
  - healthcare/healthcare/utils.py
  - healthcare/permissions.py
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - patient_portal/src/components/BookAppointmentModel.vue
---

- **Validation failures:** raise them with `frappe.throw(_("Message"), ExceptionClass, title=_("Title"))` (about 181 uses). Common titles are `_("Missing Configuration")`, `_("Not Allowed")` and `_("Mandatory")`.
- **Domain errors:** define them as **module-level subclasses of `frappe.ValidationError`** with an empty body, in the controller that raises them. Examples are `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError` and `NoActiveContractError`. Pass the class as the second argument to `frappe.throw`, for example `frappe.throw(_("Patient already has an appointment booked for the same day!"), OverlapError)`. Tests can then `assertRaises` it.
- **Background failures that must not break the user flow** (failed SMS confirmations, calendar events, patches): catch them and call `frappe.log_error(frappe.get_traceback(), _("Short Title"))` or `frappe.log_error(title=...)`. The failure is recorded in Error Log and execution continues.
- **Non-blocking info:** use `frappe.msgprint(_(...), alert=True)` on the server. On the desk client use `frappe.msgprint({...})` / `frappe.show_alert({...})`.
- **Permission denials:** `frappe.throw(_("You do not have permission ..."))` (`healthcare/permissions.py`).
- **Patient Portal:** frappe-ui `createResource` errors are shown with the `<ErrorMessage :message="error" />` component.
- Version-compatibility patches deliberately `frappe.throw(message)  # nosemgrep`. Use `# nosemgrep` only with a clear reason.
