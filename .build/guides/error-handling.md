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
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
---

- **Validation failures:** call `frappe.throw(_("Message {0}").format(...), title=_(...))`. There are ~224 call sites. Messages are translated and short, e.g. `title=_("Missing Configuration")` in `utils.py`.
- **Typed errors:** subclass `frappe.ValidationError` at module level when callers or tests need to distinguish a case. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`. Pass the class as `exc=` to `frappe.throw`.
- **Non-fatal background failures** (notifications, calendar events, patches): wrap in `try/except Exception` and record with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)` instead of failing the transaction, e.g. "Appointment Confirmation Message Not Sent".
- **Informational messages:** `frappe.msgprint` server-side. Client-side, use `frappe.show_alert` for toasts and `frappe.throw`/`frappe.msgprint` in desk JS. The portal uses `console.error` in a few catch blocks.
- **API responses:** whitelisted endpoints return plain data and raise via `frappe.throw`. Frappe serialises exceptions to the client, so there is no custom error envelope.
- Where `frappe.throw` is intentionally used in patches, it is marked `# nosemgrep`.
