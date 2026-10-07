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
  - healthcare/healthcare/utils.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
---

- **Validation errors:** raise with `frappe.throw(_("Message {0}").format(...), title=_("..."))`. There are about 181 call sites. Pass the exception class when a specific one fits, for example `frappe.throw(msg, title=_("Missing Configuration"))`.
- **Custom exceptions:** subclass `frappe.ValidationError` in the controller module that raises them (`class OverlapError(frappe.ValidationError)`, `class MaximumCapacityError(frappe.ValidationError)` in `patient_appointment.py`, `OverlapError` in `insurance_payor_contract.py`). Tests assert on these classes.
- **Non-blocking notices:** `frappe.msgprint(_(...))` (about 38 uses).
- **Swallowed or background failures:** wrap in `try/except` and record with `frappe.log_error(message_or_traceback, "Title")` so the failure shows in Error Log. Patches use the same pattern (`frappe.log_error(frappe.get_traceback(), _("... Failed"))`).
- **Intentional throws in patches:** where semgrep flags a throw that is deliberate, mark it `# nosemgrep`.
- **Messages:** always wrap them in `_()` in Python and `__()` in JS, and use `{0}` placeholders with `.format()` rather than f-strings inside `_()`.
