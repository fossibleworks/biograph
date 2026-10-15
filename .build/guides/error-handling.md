---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - healthcare/regional/india/abdm/utils.py
  - healthcare/healthcare/doctype/inpatient_medication_entry/inpatient_medication_entry.py
  - healthcare/controllers/service_request_controller.py
  - patient_portal/src/components/BookAppointmentModel.vue
---

# Error handling

- **Validation errors shown to users**: use `frappe.throw(_("message {0}").format(x))`, normally inside controller `validate`/`before_submit` methods. Pass an exception class when the meaning matters, for example `frappe.throw(_("Not allowed to print this document."), frappe.PermissionError)`. Optional kwargs include `title=_("Insufficient Stock")`, `is_minimizable=True` and `wide=True`.
- Format the message with `.format()` after `_()`, not with an f-string inside `_()`. Some legacy code does `_(f"...")`, which breaks translation; do not copy it.
- **Background or integration failures**: catch, then record with `frappe.log_error(title=..., message=..., reference_doctype=..., reference_name=...)`. Use `frappe.get_traceback(with_context=True)` for detail, as in `healthcare_payment_record.py`. Short titles are the norm ("Cant complete API call", "Failed to sync Payment Record").
- **External APIs (ABDM)**: the request/response and traceback are persisted on an `ABDM Request` doc with a status (Granted/Revoked) and also logged through `frappe.log_error`. The function then returns a safe fallback instead of raising.
- Broad `except Exception` appears in about 30 places, mostly around notifications, calendar events and history updates, so a failure there does not block the primary transaction. Do not use it around core validation.
- **Whitelisted APIs**: enforce permissions server-side. Allow-list the doctypes, and raise `frappe.PermissionError` otherwise.
- **Portal (Vue)**: resource `onError` handlers surface `err.messages?.[0]` through `toast.error` or an `<ErrorMessage>` component.
