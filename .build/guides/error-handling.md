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
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/healthcare/utils.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
---

This code follows Frappe conventions.

- **Validation and user errors:** `frappe.throw(_("message"), [ExceptionClass], title=_("..."))` (about 180 call sites). Messages are translated and use positional `{0}` placeholders with `.format(...)`. Record names and values are highlighted with `frappe.bold(...)`.
  ```python
  frappe.throw(
      _("The practitioner {0} is not available during this time due to an unavailability record {1}").format(
          frappe.bold(self.practitioner), frappe.bold(names)
      ),
  )
  frappe.throw(msg, title=_("Missing Configuration"))
  ```
- **Custom exception types** subclass `frappe.ValidationError` and are declared at the top of the controller module, for example `MaximumCapacityError`, `OverlapError`, `CoverageNotFoundError` and `NoActiveContractError`. They are passed as the second argument to `frappe.throw` so tests can `assertRaises` them.
- **Non-blocking notices** use `frappe.msgprint(...)`.
- **Background or best-effort failures** (notifications, calendar events, patches) are caught and recorded with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(title=...)`. They are not re-raised, so the main transaction still succeeds. Example: "Appointment Confirmation Message Not Sent".
- Validation lives in the DocType controller's `validate()` (and `before_submit`/`on_cancel`) methods.
- Avoid f-strings inside `_()`. Some legacy code does it, but it breaks translation extraction. Use `_("... {0}").format(x)`.
- Use `# nosemgrep` only where the Frappe semgrep rules flag an intentional pattern, as in the version-compatibility patches.
- Client side: `frappe.throw(__("..."))` / `frappe.msgprint(__("..."))` in form scripts.
