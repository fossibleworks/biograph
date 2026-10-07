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
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
---

- **Validation errors:** raise with `frappe.throw(_("Message"), [ExceptionClass], title=_("Title"))`. There are about 181 calls in the codebase.
  - Messages are translated and use `{0}` placeholders with `.format()`.
  - Row-level errors are prefixed `Row #{0}:`.
  - Typed exceptions are used where callers need to catch them (e.g. `OverlapError` for appointment overlaps).
  - Configuration gaps use `title=_("Missing Configuration")` (see `healthcare/healthcare/utils.py`).
- **Validation placement:** validations go in doctype controller hooks (`validate`, `before_submit`, …) on the server, never only in JS.
- **Non-fatal background failures** (notifications, calendar events, patches): catch them and record with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)`, so they land in the Error Log doctype and the main transaction still proceeds.
- **Informational feedback:** `frappe.msgprint` on the server; `frappe.show_alert` / `frappe.throw(__())` on the client.
- **Broad excepts:** `except Exception` appears about 31 times. Limit it to best-effort side effects and always log inside it. Note that `B904` (raise without from) is ignored in ruff.
