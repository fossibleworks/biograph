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
  - healthcare/healthcare/api/patient_portal.py
  - patient_portal/src/PatientPortal.vue
---

- **Validation errors:** raise them with `frappe.throw(_("Message."))`, about 181 call sites. Add `title=_(...)` for a dialog heading, for example `frappe.throw(msg, title=_("Customer Not Found"))`. Pass an exception class when callers or tests need to tell errors apart: `frappe.throw(_("..."), OverlapError)`.
- **Custom exceptions:** subclass `frappe.ValidationError` at module level in the doctype controller. Examples: `OverlapError` and `MaximumCapacityError` in patient_appointment; `CoverageNotFoundError` and `NoActiveContractError` in patient_insurance_coverage; `CoverageOverlapError`.
- Business logic and validation **must live on the server side** (PR template rule). Client JS may also call `frappe.throw(__('...'))` for quick input checks.
- **Non-fatal failures** (notifications, calendar events, patches) are caught and logged with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)`, so the transaction is not aborted. `except Exception` appears about 31 times. Keep it for these best-effort paths only.
- Whitelisted API functions return `None` or empty results for a missing patient or context, rather than raising (see `api/patient_portal.py`). Permission checks go through `has_website_permission` hooks.
- On the portal, frappe-ui `createResource` exposes `onSuccess`/`onError`. Problems are shown in a frappe-ui `Dialog` with a warning icon.
