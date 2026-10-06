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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
---

- **Validation errors:** use `frappe.throw(_("..."), title=_("..."))` (about 180 call sites). Messages are translatable and often use positional formatting (`_("Patient {0} is not admitted in the service unit {1}").format(...)`). Pass a specific exception class when callers or tests need to tell it apart: `frappe.throw(msg, OverlapError)`.
- **Typed errors:** define them at module level as subclasses of `frappe.ValidationError`, e.g. `MaximumCapacityError`, `OverlapError`, `CoverageNotFoundError`, `NoActiveContractError`.
- **Non-blocking notices:** `frappe.msgprint(...)`.
- **Caught failures in background or integration code:** catch them, then call `frappe.log_error(message_or_traceback, "<Title>")` so they show in the Error Log doctype, and keep the main transaction going where that is safe (e.g. calendar event creation in Patient Appointment, migration patches).
- **Patches:** wrap risky steps in try/except with `frappe.log_error(title=...)` so `migrate` does not abort on data quirks.
- **Whitelisted APIs:** rely on Frappe's permission and exception handling. Raise with `frappe.throw` and do not return error dicts.
- Semgrep (frappe rules) runs in CI. Use `# nosemgrep` only with a reason, as in `check_version_compatibility_with_frappe.py`.
