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
  - healthcare/healthcare/utils.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
  - healthcare/healthcare/api/patient_portal.py
---

- **Validation errors:** raise them with `frappe.throw(_("message"), [ExceptionClass], title=_("Title"))`. This rolls back the transaction and shows a dialog. The codebase has about 180 `frappe.throw` calls.
- **Typed errors:** when a caller or test needs to distinguish a failure, define a module-level subclass of `frappe.ValidationError` in the controller and pass it to `frappe.throw`. Examples are `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError` and `NoActiveContractError`. Tests then use `self.assertRaises(OverlapError, ...)`.
- **Configuration errors** use `title=_("Missing Configuration")` (see `healthcare/healthcare/utils.py`).
- **Background or non-fatal failures** (scheduler jobs, patches, calendar sync) are caught and recorded with `frappe.log_error(message_or_traceback, "Short Title")` so they appear in the Error Log doctype instead of breaking the user action. Avoid bare `except Exception` without logging. There are about 31 such blocks today, and new ones should log.
- **Desk JS:** client-side validation uses `frappe.throw(__("..."))`. Informational feedback uses `frappe.msgprint` or `frappe.show_alert`.
- **Whitelisted APIs:** for "not found or not applicable", return `None` or an empty result (see `get_logged_in_patient`). Throw for invalid input or permission problems.
- **Patches** that guard version compatibility call `frappe.throw(message)  # nosemgrep`.
