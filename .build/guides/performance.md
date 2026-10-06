---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/utils.py
---

These paths are likely to be performance-sensitive:

- **Wildcard doc_events.** `hooks.py` registers `"*"` handlers for `on_submit`, `on_cancel` and `on_update_after_submit` (patient medical record creation). They fire on **every submittable document in the whole ERPNext site**, so keep these handlers cheap and return early for non-healthcare doctypes.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, payment entry handlers) run on every invoice and payment. Avoid per-row queries inside item loops.
- **Scheduler:** `send_appointment_reminder` runs on the `all` schedule, every few minutes. Daily jobs update appointment, fee validity, inpatient billable and medication request statuses across whole tables. Batch the queries and use `frappe.enqueue` for long work, as `recuring_appointment_handler.py` and `sample_collection.py` already do.
- **Appointment slot and availability calculation** in `patient_appointment.py` (about 2.2k lines; overlap and capacity checks, practitioner schedules) is called interactively from the booking UI and the portal.
- **Portal APIs** (`api/patient_portal.py`) use single `frappe.qb` joins. Keep that pattern and avoid N+1 lookups. Note that `get_appointments` currently calls `get_patients_with_relations()` twice.
- **Indexes:** doctype JSON uses `search_index` (about 119 fields), e.g. on `patient` and `procedure_template`. Add `search_index` to new link fields that list views, reports or filters query.
