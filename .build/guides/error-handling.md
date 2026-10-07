---
title: Error handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/public/js/sales_invoice.js
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
---

- **Validation errors that users see:** use `frappe.throw(_("..."))`, which appears about 181 times in the Python code. Pass `title=_("...")` where it helps, e.g. `title=_("Missing Configuration")` or `_("Not Available")`. Pass a specific exception class when callers or tests need to tell errors apart.
- **Custom exceptions:** subclass `frappe.ValidationError` inside the controller module, e.g. `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`. Raise them as `frappe.throw(msg, OverlapError)`.
- **Non-fatal problems:** for failures such as an SMS or confirmation that was not sent, or a calendar event that could not be cancelled, catch the exception. Then call `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(message=..., title=...)`, and tell the user with `frappe.msgprint(..., indicator="orange")` or `alert=True`.
- **Success feedback:** `frappe.msgprint(_("Sales Invoice {0} created").format(name), alert=True)`.
- **Desk JS:** `frappe.throw(__("Please select a Patient to be invoiced"))` guards user actions on the client.
- **Portal:** frappe-ui `createResource` `onSuccess` / `onError` handlers show a frappe-ui `Dialog` with a warning icon.
- **Semgrep:** patches that deliberately throw are annotated `# nosemgrep`.
