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
  - healthcare/controllers/service_request_controller.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/setup.py
  - healthcare/permissions.py
  - .github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md
---

- **User and validation errors:** raise with `frappe.throw(_("...").format(...), title=_("..."))`. The codebase has about 181 calls. Wrap identifiers with `frappe.bold()` where helpful, for example `_("Please set Customer in Patient {0}").format(frappe.bold(self.patient))`.
- **Typed errors:** define module-level subclasses of `frappe.ValidationError`, such as `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError` and `CoverageOverlapError`. Pass them as `frappe.throw(msg, exc=OverlapError)` so tests can `assertRaises` them.
- **Non-blocking notices:** use `frappe.msgprint` (about 38 calls).
- **Catching:** catch specific Frappe exceptions such as `frappe.DoesNotExistError` and `frappe.DuplicateEntryError`, then re-throw a translated message or skip. Broad `except Exception` appears in background and best-effort paths, and must be paired with `frappe.log_error(...)`.
- **Background or side-effect failures:** use `frappe.log_error(title=..., message=...)` (about 15 calls) so the failure lands in the Error Log DocType. Do not swallow it silently.
- **API endpoints:** whitelisted functions rely on Frappe converting `frappe.throw` into an HTTP error with `_server_messages`. Do not return ad-hoc error dicts. Use `frappe.has_permission` / `frappe.throw(..., frappe.PermissionError)` for access checks (see `permissions.py`).
- **Desk JS:** use `frappe.throw(__("..."))` for client validation and `frappe.msgprint(__("..."))` for notices. The PR template states that **all business logic and validations must be on the server side**.
