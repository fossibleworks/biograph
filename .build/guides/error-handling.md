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
  - healthcare/healthcare/utils.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
---

- **User-facing validation:** `frappe.throw(_("message"), [ExceptionClass], title=_("Title"))`. This rolls back the transaction and shows a dialog. There are about 180 uses.
- **Typed errors:** define module-level subclasses of `frappe.ValidationError` for conditions that tests or callers need to catch, e.g. `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`. Pass them as the second argument: `frappe.throw(_(...), OverlapError)`.
- **Missing configuration:** use `frappe.throw(msg, title=_("Missing Configuration"))` (see `healthcare/healthcare/utils.py`).
- **Non-blocking failures** (notifications, calendar events, patches): catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("Title"))` so it shows in the Error Log DocType. Do not re-raise when the main operation should still succeed.
- **Informational messages:** use `frappe.msgprint`.
- **Client side:** `frappe.throw(__("..."))` in form JS is only for immediate UI validation. The authoritative check must also exist on the server.
- Only suppress semgrep with `# nosemgrep` when the throw is intentional (as in the patches).
