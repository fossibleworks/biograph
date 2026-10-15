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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/doctype/lab_test/lab_test.py
---

# Error handling

- **Validation errors shown to users:** use `frappe.throw(_("message {0}").format(x), title=_("..."))`. This is the dominant pattern, with about 181 call sites. Pass an exception class when it matters, e.g. `frappe.throw(..., frappe.PermissionError)` for access checks in portal APIs.
- **Domain exceptions:** subclass `frappe.ValidationError` (e.g. `OverlapError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`) so tests can assert on them.
- **Non-fatal warnings:** use `frappe.msgprint(_(...), title=_("Warning"))` or `alert=True`.
- **Background or scheduled work:** wrap per-record work in `try/except Exception`, record it with `frappe.log_error(title=..., message=frappe.get_traceback())` and continue. Re-`raise` when the failure must abort, as in inpatient billing.
- **Avoid:** swallowing exceptions silently, and putting raw `str(e)` into user messages without translation (this exists in `patient_encounter.py` but is not the preferred pattern).
- Permission checks should use Frappe permissions (`frappe.has_permission`, `has_website_permission` hooks) rather than ad-hoc checks.
