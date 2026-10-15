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
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/lab_test/lab_test.py
---

- **User-facing validation:** `frappe.throw(_("message {0}").format(x), title=_("..."))` is the standard. It appears about 159 times. Throw it from controller hooks (`validate`, `before_submit`, …) or whitelisted methods. Pass an exception class when callers or tests need to catch it, for example `frappe.throw(msg, frappe.PermissionError)` or `frappe.throw(msg, title=_("Missing Configuration"))`.
- **Custom exceptions:** subclass `frappe.ValidationError` in the controller module, for example `OverlapError`, `MaximumCapacityError` and `CoverageNotFoundError`. Tests assert them with `assertRaises`.
- **Warnings that don't block:** `frappe.msgprint(_("..."), title=_("Warning"))` or `alert=True`.
- **Background or best-effort work** (scheduler jobs, notifications, billing side-effects): catch `Exception` and record it with `frappe.log_error(title=..., message=frappe.get_traceback())` so it shows in the Error Log doctype, then continue. Examples are medication request expiry and appointment confirmation messages. Prefer the `title=` + traceback form over `log_error(f"...{str(e)}")`.
- **Permissions:** `frappe.throw(..., frappe.PermissionError)`. Portal APIs check ownership before returning documents.
- Avoid bare `except Exception:` that swallows errors silently. Avoid showing raw exception text to users. A few existing spots do both, for example in `patient_encounter.py`. Do not copy them.
