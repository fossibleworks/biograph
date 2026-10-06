---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/hooks.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/fee_validity/fee_validity.py
---

These are the paths most likely to be performance-sensitive:

- **Appointment scheduling**
  - `patient_appointment.py` is about 2,200 lines.
  - It contains `get_availability_data`, `get_available_slots` and the overlap/capacity checks, all of which run raw SQL per booking and per slot lookup.
  - The portal's `api/patient_portal.get_slots` calls into the same code.
  - Keep the queries indexed. The fork added `search_index` on hot link fields such as `patient` and `procedure_template`.
  - Avoid per-slot database round-trips.
- **Wildcard doc_events**
  - `hooks.py` registers `"*": on_submit/on_cancel/on_update_after_submit` → `patient_history_settings.create/delete/update_medical_record`.
  - This runs on every submit across all of ERPNext, so keep it cheap and return early.
- **Billing hooks**
  - Sales Invoice validate/submit/cancel and Payment Entry hooks run inside ERPNext's accounting transactions (`healthcare/healthcare/utils.py`).
- **Scheduler**
  - `send_appointment_reminder` runs on `all` (every tick).
  - Daily jobs update appointment and fee-validity status, add inpatient billables and expire medication requests.
  - These jobs scan whole tables, so use filtered `frappe.get_all` / `frappe.qb` and batch the work.
- **Reports and pages**
  - Reports under `healthcare/healthcare/report/` (patient_appointment_analytics, lab_test_report, diagnosis_trends) and the `patient_history` / `patient_progress` pages aggregate over large clinical datasets.

**Conventions to follow**
- Use `frappe.get_cached_value` / `get_cached_doc` for settings and master data. `Healthcare Settings` is read often.
- Use `frappe.enqueue` for long work; it is used very little today.
- Prefer `frappe.qb` or parameterized SQL with selective columns over `get_doc` in loops.
