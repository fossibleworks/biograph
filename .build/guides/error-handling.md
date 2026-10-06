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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/patches/v15_0/check_version_compatibility_with_frappe.py
  - healthcare/healthcare/api/patient_portal.py
---

**Validation errors shown to users:** raise them with `frappe.throw(_("…"), title=_("…"))`. There are about 180 call sites.
- Messages are translated and use `{0}` placeholders filled with `.format(...)`, often with `get_link_to_form` for links (for example, `_("{0} is a holiday")`).
- Use an optional `title`, such as `title=_("Missing Configuration")` in `utils.py`.
- For a typed error, subclass `frappe.ValidationError` (`class OverlapError(frappe.ValidationError)`) and pass it as `exc=` to `frappe.throw`.

**Non-fatal notices:** use `frappe.msgprint(_("…"))`, for example `"Sales Invoice {0} created"` or `"SMS not sent, please check SMS Settings"`.

**Background, notification and patch failures:** catch the exception and record it with `frappe.log_error(frappe.get_traceback(), _("<Title>"))` or `frappe.log_error(title=...)` so it appears in the Error Log, then continue. Examples are appointment confirmation SMS and unavailability calendar events. Patches wrap risky steps in `try/except` and log the failure.

**API endpoints** (`api/patient_portal.py`) return `None` or an empty result for missing data instead of raising, and rely on Frappe's permission system and whitelisting.

**Cautions**
- About 31 `except Exception` blocks exist. Keep them limited to logging and best-effort side effects; do not swallow them on validation paths.
- ruff's B904 (raise from) is ignored.
- Mark intentional `frappe.throw` calls in patches with `# nosemgrep`.
