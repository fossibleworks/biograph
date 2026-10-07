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
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
---

# Error handling

- **User-facing validation:**
  - Raise with `frappe.throw(_("message"), [ExcClass], title=_("Title"))`. There are about 181 call sites.
  - Messages are translatable sentences, often with `{0}` placeholders filled via `.format()` *after* `_()`.
  - Common titles include `Missing Configuration` and `Not Available`.
- **Typed errors:** define module-level subclasses of `frappe.ValidationError` in the controller and pass them to `frappe.throw` so tests can `assertRaises` them. Examples: `OverlapError`, `MaximumCapacityError`, `CoverageNotFoundError`, `NoActiveContractError`.
- **Non-blocking notices:** `frappe.msgprint(_(...))` (about 38 uses).
- **Unexpected or background failures:** catch, then record with `frappe.log_error(title=..., message=...)` or `frappe.log_error(frappe.get_traceback(), title)`. This creates an Error Log doc. Patches and calendar sync use this pattern instead of failing the request.
- Use `get_link_to_form()` inside messages to link the offending document.
- Validate on the server (`validate`, `before_submit` hooks), not only in JS.
- Silencing semgrep with `# nosemgrep` is reserved for intentional throws in patches.
