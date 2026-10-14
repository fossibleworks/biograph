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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

**Validation errors (user-facing)**
- Raise them with `frappe.throw(_("message {0}").format(...), [ExceptionClass], title=_("Title"))`. There are about 181 uses. Highlight key values with `frappe.bold(...)`.
- For conditions that tests or callers need to catch, define a domain exception that subclasses `frappe.ValidationError` in the controller module, e.g. `OverlapError` and `MaximumCapacityError` in `patient_appointment.py`, and `CoverageNotFoundError` and `NoActiveContractError` in `patient_insurance_coverage.py`. Pass it as the second argument to `frappe.throw`.
- Put validation in the server-side controller (`validate`, `before_submit`, …), not only in JS (PR template rule).
- Use `title=_("Missing Configuration")` when a required Healthcare Settings value is missing (see `healthcare/healthcare/utils.py`).

**Non-blocking notices**
- Use `frappe.msgprint(_(...))` on the server (about 38 uses) and `frappe.msgprint(__(...))` / `frappe.show_alert` in Desk JS.

**Background / side-effect failures**
- Wrap these in `try/except Exception` and record them with `frappe.log_error(frappe.get_traceback(), _("Title"))` (or `frappe.log_error(title=...)`) so the main transaction is not blocked. Examples: notification sending ("Appointment Confirmation Message Not Sent"), calendar events, and patches.
- Patches catch exceptions, log them and continue.

**Portal (Vue)**
- `createResource` errors are shown with frappe-ui `ErrorMessage` or `toast`.

Do not swallow exceptions silently. Do not raise bare `Exception` for user errors. Avoid `print`.
