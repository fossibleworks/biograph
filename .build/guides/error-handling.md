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
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
---

- **Validation failures:** use `frappe.throw(_("Message with {0}").format(...))` (about 181 call sites). Messages are translated, use sentence case, and often include `get_link_to_form(...)` or the field value.
- **Typed errors:** declare domain exceptions at module top as subclasses of `frappe.ValidationError` (`OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`) and pass them via `frappe.throw(msg, exc=OverlapError)` so tests can assert on them.
- **Non-fatal background failures** (SMS or confirmation not sent, calendar event errors, patch steps): catch the exception and call `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)` so the main transaction can continue. Do not swallow errors silently.
- **Patches:** guard risky steps with try/except plus `frappe.log_error` so `bench migrate` does not abort.
- **API endpoints:** whitelisted functions raise through `frappe.throw` / permission errors. Frappe turns these into HTTP error responses, and the portal shows them via frappe-ui `ErrorMessage`.
