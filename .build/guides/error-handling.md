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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/public/js/sales_invoice.js
  - patient_portal/src/PatientPortal.vue
---

- **Validation errors:** call `frappe.throw(_("message"), ExcClass, title=_("…"))` about 181 times across the codebase. Messages are translated and may use `.format()` placeholders. Common titles include `_("Missing Configuration")`.
- **Custom exceptions:** subclass `frappe.ValidationError` in the controller module, as in `MaximumCapacityError` and `OverlapError` in `patient_appointment.py` and `OverlapError` in `insurance_payor_contract.py`. Tests can then assert on the specific class.
- **Controller hooks:** put validation in `validate()`, `before_submit()` and similar methods, not in whitelisted endpoints.
- **Background or non-fatal failures:** catch broad exceptions and record them with `frappe.log_error(message_or_traceback, title)` rather than failing silently. Patches and calendar-event sync follow this pattern.
- **Patches:** may log and continue. The compatibility-check patches use `frappe.throw` with `# nosemgrep`.
- **Client side:** desk JS shows `frappe.msgprint(__("…"))` for blocking messages and `frappe.show_alert({message, indicator})` for transient ones. The Vue portal resources use `onError(error)` and read `error.messages?.[0]`.
