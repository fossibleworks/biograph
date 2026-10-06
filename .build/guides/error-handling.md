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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
---

- **Validation errors:** call `frappe.throw(_("..."))`, about 180 uses. Add `title=_("...")` when grouping makes sense (for example `title=_("Missing Configuration")` in `utils.py`, or `title=_("Not Available")`). Messages should name the offending record using `{0}` placeholders or `get_link_to_form`.
- **Typed errors:** subclass `frappe.ValidationError` near the controller (`OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`). Pass the class as the exception argument: `frappe.throw(msg, OverlapError)`. Tests assert on these classes.
- **Non-blocking failures** (SMS, notifications, calendar events, patches): wrap them in `try/except`. Record the failure with `frappe.log_error(frappe.get_traceback(), _("<Title>"))`, which goes to the Error Log DocType. Optionally show a `frappe.msgprint(..., indicator="orange")` or `alert=True` message instead of failing the transaction, as in `Appointment Confirmation Message Not Sent`.
- **Informational feedback:** use `frappe.msgprint(_("Sales Invoice {0} created").format(name), alert=True)`.
- **Patches:** guard risky steps and call `frappe.log_error(title=...)` so a failing patch does not abort the whole migrate. Compatibility checks may `frappe.throw` (marked with `# nosemgrep`).
- Avoid bare `except:` and swallowed exceptions with no log. Semgrep (Frappe rules) runs in CI.
