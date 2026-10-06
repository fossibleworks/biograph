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
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
---

# Error handling

## Validation errors (dominant pattern)
- Raise user-facing errors with **`frappe.throw(_("Message"))`**. Use `.format()` placeholders outside `_()`: `frappe.throw(_("Configure a service Item for {0}").format(item))`. Optional `title=_("...")`.
- For distinct failure modes, define subclasses of **`frappe.ValidationError`** in the controller module (`class OverlapError(frappe.ValidationError)`, `MaximumCapacityError`) and pass them as the exception class: `frappe.throw(msg, OverlapError)`. Tests can then assert the specific class.
- Validation belongs in the controller lifecycle hooks (`validate`, `before_submit`, `on_cancel`, ...).

## Non-fatal / background failures
- Side effects such as notifications and calendar events, and patches, catch exceptions and record them with **`frappe.log_error(frappe.get_traceback(), _("Title"))`** or `frappe.log_error(title=...)`, without failing the main transaction (for example, "Appointment Confirmation Message Not Sent").
- `frappe.logger().error(...)` is used occasionally for parse failures.
- Do not swallow exceptions silently. Log them to Error Log.

## JS
- Desk scripts surface problems with `frappe.msgprint` / `frappe.throw` and translatable `__()` strings.

## Avoid
- `frappe.throw(_("... {0}".format(x)))`: formatting *inside* `_()` breaks translation. It exists in legacy code (`patient_appointment.py`), so don't copy it.
