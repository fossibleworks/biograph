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
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/patches/v16_0/check_v16_compatibility_with_frappe.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/public/js/healthcare_practitioner.js
---

# Error handling

- **User-facing validation:** use `frappe.throw(_("Message {0}").format(x), [ExcClass], title=_("Title"))`. The codebase has about 181 `frappe.throw` calls. Domain errors subclass `frappe.ValidationError` so tests and callers can catch them precisely (`OverlapError`, `MaximumCapacityError`). Use `title=_("Missing Configuration")` for settings or account gaps (see `utils.py`). Add links with `get_link_to_form`.
- **Non-blocking notices:** `frappe.msgprint(_(...), alert=True)`.
- **Background or best-effort failures** (SMS/notifications, calendar events, scheduler billing, patches): catch the exception and record it with `frappe.log_error(...)`, giving a short human title such as `"Appointment Confirmation Message Not Sent"` or `"Can't bill Service Unit occupancy"`. Usually pass `frappe.get_traceback()` as the message. Don't re-raise when the main transaction should still succeed.
- **Patches:** compatibility checks `frappe.throw` to abort a migration (marked `# nosemgrep`).
- **Desk JS:** `frappe.throw(__('...'))` for client-side validation.
- **Portal (Vue):** surface API errors with frappe-ui `toast.error(err.messages?.[0] || err)` or `<ErrorMessage>`.
- Wrap every message in `_()` / `__()`. Some legacy calls pass raw or pre-formatted strings (`_("{0} is a holiday".format(date))`); don't copy that. Format **after** `_()`.
