---
title: Error Handling
category: error-handling
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/utils.py
  - healthcare/controllers/service_request_controller.py
  - healthcare/public/js/mark_unavailable.js
  - patient_portal/src/components/Payment.vue
---

## User-facing validation errors

- Raise errors with **`frappe.throw(_("message"), ExcClass, title=_("Title"))`**. There are about 180 call sites. Frappe rolls back the transaction and shows a dialog.
- When callers or tests need to tell errors apart, define a domain exception in the DocType module that subclasses `frappe.ValidationError`. Examples are `OverlapError` and `MaximumCapacityError` (patient_appointment), `CoverageNotFoundError` and `NoActiveContractError` (patient_insurance_coverage), and `CoverageOverlapError`. Pass the class as the second argument to `frappe.throw`.
- Titles are short title-case nouns, for example `title=_("Missing Configuration")` or `title=_("Not Allowed")`. Use `get_link_to_form()` in messages that point at a record.
- For non-blocking warnings, use `frappe.msgprint(_("..."), indicator="orange")`.

## Side effects that must not block the transaction

For SMS, calendar events, payment sync, and scheduler billing, wrap the call in `try/except Exception` and record it with **`frappe.log_error`**. Then optionally `msgprint` a warning:

```python
except Exception:
	frappe.log_error(
		title="Failed to sync Payment Record",
		message=f"Exception:\n{frappe.get_traceback(with_context=True)}\n",
		reference_doctype=self.doctype,
		reference_name=self.name,
	)
```

Prefer this keyword form (title, traceback, reference doc) over positional `frappe.log_error(msg)`.

## Client side

Desk JS uses `frappe.throw(__('...'))` for input validation and `frappe.msgprint({...})` for notices. The Vue portal shows API errors with frappe-ui's `ErrorMessage` component.
