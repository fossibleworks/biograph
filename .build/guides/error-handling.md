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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
---

- **Validation errors:** raise them with **`frappe.throw(_("Message"))`** (about 180 uses).
  - Pass `title=_("...")` to group errors, for example `title=_("Missing Configuration")` or `title=_("Not Available")`.
  - Interpolate values with `_("... {0}").format(value)`, not f-strings inside `_()`. Older code violates this.
  - Highlight names with `frappe.bold()`.
- **Typed errors:** subclass `frappe.ValidationError` per module and pass the class to throw, for example `frappe.throw(msg, OverlapError)`. Existing examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`. Tests can then assert on the class.
- **Non-blocking messages:** use `frappe.msgprint`.
- **Background or best-effort work:** catch `Exception`, then record it with `frappe.log_error(message_or_traceback, "Title")` and use `frappe.get_traceback()` for detail. Do not swallow errors silently. Do not use `print()`, even though some legacy appointment code does.
- **Patches:** guard risky renames with try/except and `frappe.log_error`. Version-compatibility patches throw on purpose (marked `# nosemgrep`).
- **Client side:** desk JS uses `frappe.msgprint` and `frappe.throw` with `__()` strings.
