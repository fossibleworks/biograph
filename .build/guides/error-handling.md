---
title: Error handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/public/js/sales_invoice.js
---

# Error handling

## Validation errors
- Use **`frappe.throw(_("message"), [ExcClass], title=_("Title"))`**. There are about 180 uses, and it is the dominant pattern. It raises `frappe.ValidationError` and shows a dialog in Desk.
- Messages are translated with `_()`, interpolated with `.format()` and `{0}` placeholders, and often use `frappe.bold(name)` to highlight document names.
- For domain-specific failures, define a module-level subclass of `frappe.ValidationError` in the controller module and pass it to `frappe.throw`:
  - `OverlapError` and `MaximumCapacityError` in `patient_appointment.py`
  - `CoverageNotFoundError` and `NoActiveContractError` in `patient_insurance_coverage.py`
  - Tests then assert on the specific class.
- Use `frappe.msgprint` for non-fatal warnings and info.
- In JS, use `frappe.msgprint(__())` / `frappe.show_alert({...})`.

## Background and unexpected failures
- In scheduler jobs, notifications and patches, catch the exception and record it with **`frappe.log_error(frappe.get_traceback(), _("Short Title"))`** (or `log_error(title=...)`) instead of failing the whole job.
- Example: appointment confirmation messages.
- `frappe.logger().info/error` is used occasionally in patches.

## API endpoints
- Whitelisted functions raise through `frappe.throw` and Frappe converts that to the HTTP error response.
- Use `frappe.PermissionError` / `frappe.DoesNotExistError` for access and missing records.
- The portal surfaces these errors through frappe-ui resources and `ErrorMessage`.
