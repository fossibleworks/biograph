---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/healthcare_practitioner/healthcare_practitioner.py
  - healthcare/setup.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/permissions.py
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
---

- **Validation failures:** call `frappe.throw(_("Message {0}").format(...), title=_("..."))`. There are about 180 `frappe.throw` calls in Python. Pass an exception class when callers or tests need to tell errors apart, e.g. `frappe.throw(_(msg), frappe.ValidationError)`. Frappe rolls back the transaction and shows the message.
- **Custom error types** subclass `frappe.ValidationError` and live in the controller module, e.g. `MaximumCapacityError` and `OverlapError` in `patient_appointment.py`.
- **Messages that should not block:** `frappe.msgprint(...)` (about 38 uses). In Desk JS, use `frappe.msgprint(__(...))` or `frappe.throw(__(...))` for client-side guards. Server-side validation is still required.
- **Side effects that may fail** (SMS/notifications, calendar events, patches) are wrapped in `try/except Exception` and logged with `frappe.log_error(frappe.get_traceback(), _("Short Title"))` or `frappe.log_error(title=...)` instead of being re-raised. For example, a failed appointment-confirmation SMS logs *Appointment Confirmation Message Not Sent* and the save still succeeds.
- **Expected races and duplicates in setup code:** catch the specific exception, e.g. `except frappe.DuplicateEntryError:` in `setup.py`.
- **Permissions:** `healthcare/permissions.py` throws a permission error for unauthorised access.
- Semgrep (Frappe rules) is enforced in CI. Suppress a rule only with an inline `# nosemgrep` and a reason, as in `check_version_compatibility_with_frappe.py`.
