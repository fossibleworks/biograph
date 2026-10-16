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
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/setup.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
  - healthcare/public/js/sales_invoice.js
---

- **User and validation errors:** `frappe.throw(_("Message {0}").format(val))` raises a `ValidationError` and shows a dialog. This is the dominant pattern, with about 181 calls. Give context with `title=_("Missing Configuration")` or pass an exception class: `frappe.throw(msg, frappe.ValidationError)`.
- **Custom error types:** subclass `frappe.ValidationError` near the controller that uses them, for example `MaximumCapacityError` and `OverlapError` in patient_appointment and insurance_payor_contract. Tests then assert on the specific class.
- **Background or best-effort failures:** in schedulers, notifications and patches, catch the exception and call `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)` rather than crash. Examples: appointment confirmation SMS, unavailability calendar events, patch migrations.
- **Expected framework errors:** catch them narrowly, for example `except frappe.DuplicateEntryError:` in setup.
- **Broad `except Exception` blocks:** use them only around non-critical side effects, and always log.
- **Desk JS:** warnings go through `frappe.msgprint(__("..."))`, toast feedback through `frappe.show_alert({message, indicator})`.
- **Semgrep:** a `# nosemgrep` marker appears on dynamic `frappe.throw(message)` calls whose message is already translated.
