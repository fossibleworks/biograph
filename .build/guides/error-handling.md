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
  - healthcare/patches/v15_0/rename_medical_code_standard_and_medical_code.py
  - healthcare/permissions.py
  - patient_portal/src/components/Payment.vue
---

**Validation errors:**
- Raise them with `frappe.throw(msg, title=_(...))`. This is the dominant pattern, with about 223 calls.
- Messages are translated and often link to the offending record via `get_link_to_form`. Example: `frappe.throw(msg, title=_("Missing Configuration"))` in `healthcare/healthcare/utils.py`.
- For domain-specific errors, subclass `frappe.ValidationError` (`OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`) and pass the class to `frappe.throw(..., exc=...)`. Tests can then assert on it.
- Use `frappe.PermissionError` for permission failures (see `healthcare/permissions.py`).

**Non-fatal user feedback:**
- Server side: `frappe.msgprint(...)` or `frappe.msgprint(..., alert=True)`.
- Desk JS: `frappe.msgprint(__(...))` and `frappe.show_alert({...})`.

**Background, integration, and patch failures:**
- Catch the exception and record it with `frappe.log_error(message_or_traceback, title)` so it appears in Error Log, e.g. appointment confirmation messages, calendar events, and patches.
- Re-raise unless the failure is truly optional. In patches, the existing pattern checks DB error codes and re-raises anything unexpected.

**Anti-patterns:** bare `except Exception: pass` and `print(f"ERROR - ...")` both exist in the code, for example in `recuring_appointment_handler.py` and `patient_appointment.py`. Do not copy them.

**Portal (Vue):** surface errors from frappe-ui resources with the `ErrorMessage` component.
