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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
  - healthcare/public/js/sales_invoice.js
---

- **User-facing validation errors:** call `frappe.throw(_("...").format(...), title=_("..."))` (about 180 call sites). Messages are translated and often link to the offending record with `get_link_to_form`, e.g. a `title=_("Missing Configuration")` throw that links to Healthcare Settings.
- **Typed errors:** define module-level subclasses of `frappe.ValidationError` when callers or tests need to tell errors apart (`OverlapError`, `MaximumCapacityError`), and raise them with `frappe.throw(msg, exc=OverlapError)`.
- **Non-fatal / background failures:** catch the exception and call `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(title=...)` so the failure is recorded in Error Log without breaking the user flow (appointment confirmation messages, calendar events, patches).
- **Desk JS:** use `frappe.throw(__("..."))` to block an action, `frappe.msgprint(__("..."))` for informational prompts, and `frappe.show_alert({...})` for toasts.
- **Patches:** stay idempotent. Wrap risky steps and log the error instead of aborting the migration where that is safe. A deliberate abort uses `frappe.throw` with `# nosemgrep`.
- Don't swallow errors silently. Every caught exception in existing code is either logged or re-thrown.
