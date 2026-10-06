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
  - healthcare/setup.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
---

- **Validation errors:** raise them with `frappe.throw(_("Message"), [ExcClass], title=_("Title"))`. This is by far the most common pattern (about 180 call sites). Frappe turns it into a user-facing dialog and rolls back the transaction.
- **Domain exception types:** declare them at module top as subclasses of `frappe.ValidationError`, for example `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError` and `NoActiveContractError`. Pass them as the second argument to `frappe.throw` so callers and tests can `assertRaises` them. Use Frappe's built-ins where they fit: `frappe.PermissionError`, `frappe.DoesNotExistError`, `frappe.DuplicateEntryError`.
- **Non-fatal problems:** for side effects like SMS or notifications, catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("Title"))` so it shows up in the Error Log doctype. Use `frappe.msgprint(_("..."))` for informational notices.
- **Idempotent setup:** setup and patches catch specific exceptions, for example `except frappe.DuplicateEntryError:` in `setup.py`.
- **Translations:** put messages through `_()` and use `{0}` placeholders with `.format()`. Avoid f-strings inside `_()`, because they break translation extraction.
- `# nosemgrep` is used only for deliberate exceptions, such as throws in version-compatibility patches.
