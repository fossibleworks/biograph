---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/healthcare_settings/healthcare_settings.py
---

# Error handling

## Server (Python)
- **Validation errors** are raised with `frappe.throw(_("Message {0}").format(x))`. The repo has about 180 call sites. Add `title=_("...")` for context (e.g. `title=_("Missing Configuration")`) and pass an exception class when it matters: `frappe.throw(_("Not allowed to print this document."), frappe.PermissionError)`.
- **Domain exception classes** subclass `frappe.ValidationError` and are defined at the top of the DocType module: `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`, `CoverageOverlapError`. Tests assert on these specific classes.
- **Background or best-effort work** (schedulers, notifications, billing side effects) catches the exception and records it with `frappe.log_error(...)` instead of failing the transaction. For example: `frappe.log_error(message=e, title="Can't bill Service Unit occupancy")`, `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`.
- Validation belongs in controller hooks (`validate`, `before_submit`) on the server, not only in the client.

## Client (desk JS)
- Use `frappe.throw(__("..."))` to block an action, `frappe.msgprint(__("..."))` for informational dialogs, and `frappe.show_alert({message: __("..."), indicator: "green"|"red"})` for toasts.
