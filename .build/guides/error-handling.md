---
title: Error handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/setup.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

- **User and validation errors:** raise them with **`frappe.throw(_("message"), [ExcClass], title=_(...))`**. This is about 181 call sites in Python. Messages are translatable and use `.format()` placeholders, e.g. `frappe.throw(_("Invalid Code Value: {0}").format(code_value))`, or `frappe.throw(msg, title=_("Missing Configuration"))`.
- **Typed errors:** domain-specific subclasses of **`frappe.ValidationError`** are declared at the top of the controller module and passed to `frappe.throw`. Examples are `OverlapError`, `MaximumCapacityError` (patient_appointment), `CoverageOverlapError`, `CoverageNotFoundError` and `NoActiveContractError`. Tests can assert on these types.
- **Non-fatal failures** (notifications, calendar events, background jobs) are caught and recorded with **`frappe.log_error(...)`**, usually `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(message=e, title="...")`. The main transaction is not aborted.
- **Idempotent setup:** catch specific Frappe exceptions such as `except frappe.DuplicateEntryError:` in `setup.py`. Broad `except Exception` mostly appears in patches and uninstall.
- **Patches:** compatibility guards use `frappe.throw(message)  # nosemgrep`.
- **Desk JS:** use `frappe.throw(__("..."))` for blocking client checks and `frappe.msgprint({...})` for informational dialogs. Some legacy JS strings are unwrapped or contain inline `<b>` HTML. Prefer `__()` in new code.
- The PR template requires the authoritative validation to live server-side.
