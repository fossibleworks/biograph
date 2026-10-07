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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/patient_encounter/patient_encounter.js
---

- **Validation errors:** raise them with `frappe.throw(_("Message"), [ExceptionClass])`. There are about 180 call sites. Frappe rolls back the transaction and shows the message to the user.
- **Typed errors:** define a module-level subclass of `frappe.ValidationError` when callers or tests need to tell errors apart. Examples: `OverlapError` and `MaximumCapacityError` in `patient_appointment.py`, and `OverlapError` in `insurance_payor_contract.py`. Pass the class as the second argument to `frappe.throw`.
- **Permissions:** whitelisted APIs check access and throw `frappe.PermissionError`, e.g. `frappe.throw(_("Not allowed to print this document."), frappe.PermissionError)` in `api/patient_portal.py`.
- **Best-effort side effects** (notifications, calendar events, patches): wrap them in `try/except Exception` and record the failure with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(message=..., title=...)`, so the main transaction is not aborted.
- **Messages:** short, sentence-case, translated, and they end with a period. Use `{0}` placeholders with `.format()`.
- **Client side:** use `frappe.msgprint(__("..."))` for blocking notices and `frappe.show_alert({message, indicator})` for transient ones.
