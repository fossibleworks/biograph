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
  - healthcare/permissions.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
---

- **Validation failures:** raise with `frappe.throw(_("..."))` (about 180 call sites). Pass a `title=_("...")` where it helps, e.g. `title=_("Missing Configuration")`. Pass a specific exception class for callers or tests that need to catch it.
- **Custom exceptions** subclass `frappe.ValidationError` and are defined in the controller module: `OverlapError`, `MaximumCapacityError`, `CoverageOverlapError`, `NoActiveContractError`. Permission failures use `frappe.PermissionError` (`healthcare/permissions.py`).
- **Messages** are translated and formatted with `.format()`. Wrap document names in `frappe.bold()`, e.g. `_("Patient {0} is not admitted in the service unit {1}").format(...)`.
- **Non-fatal background failures** (notifications, calendar sync, patches) are caught. They are recorded with `frappe.log_error(frappe.get_traceback(), _("<Title>"))` instead of re-raised, so the main transaction still completes.
- **Warnings without aborting:** `frappe.msgprint`. In desk JS use `frappe.msgprint({...})` / `frappe.show_alert`.
- **Patient portal (Vue):** frappe-ui resources use `onError(e)` handlers. They show `toast.error(err.messages?.[0] || err)` or an `<ErrorMessage :message="error" />` component.
