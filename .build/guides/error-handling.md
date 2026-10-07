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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
  - healthcare/healthcare/doctype/patient/patient.py
---

- **Validation errors:** raise them with `frappe.throw(_("message {0}").format(x))`. There are about 180 uses. Pass `title=_("Missing Configuration")` for configuration problems, as `utils.py` does. Row-level messages follow the `"Row #{0} (Section): …"` pattern.
- **Typed errors:** subclass `frappe.ValidationError` at module level and raise with `frappe.throw(msg, exc=...)`. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `CoverageNotFoundError`, `NoActiveContractError`. Tests assert on these types.
- **Non-blocking notices:** use `frappe.msgprint(_(...), alert=True, indicator="warning")`.
- **Background or side-effect failures** (notifications, calendar events, payments, patches): catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("Title"))` or `frappe.log_error(message=..., title=...)` so the main transaction is not blocked. The message ends up in the Error Log doctype.
- Avoid bare `except Exception` that swallows errors silently. There are about 31 existing instances; new code should log them or re-raise.
- Untranslated throws such as `frappe.throw("Slots are not available")` exist, but they are legacy. `# nosemgrep` is used only on deliberate untranslated throws in compatibility patches.
- **Client side:** `frappe.call` callbacks plus `frappe.msgprint` / `frappe.show_alert` with `__()` strings.
