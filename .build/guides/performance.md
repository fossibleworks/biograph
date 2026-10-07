---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
  - patient_portal/vite.config.js
---

Paths likely to be performance-sensitive:

- **Global `doc_events["*"]`:** `create_medical_record`, `delete_medical_record` and `update_medical_record` run on submit, cancel and update-after-submit of *every* doctype. Keep them cheap, and return early when Patient History Settings do not apply.
- **Scheduler jobs:** `send_appointment_reminder` runs on the `all` (every few minutes) schedule. Daily jobs update appointment status, fee validity, inpatient occupied-unit billables, and expired medication requests. These loop over potentially large tables, so query with filters and fields, not full `get_doc` loops.
- **Appointment slot lookup:** `get_availability_data` in `patient_appointment.py` and `get_slots` / `make_appointment` in `api/patient_portal.py` loop over practitioner schedules and service units per request. They are hit interactively from the desk calendar and the portal.
- **ERPNext billing hooks:** Sales Invoice validate/submit/cancel and Payment Entry hooks (`manage_invoice_validate`, `set_paid_amount_in_healthcare_docs`) add work to every invoice and payment.
- **Raw SQL:** about 91 `frappe.db.sql` call sites. Use parameterized queries and indexed fields. Doctype JSON sets `search_index` on hot link fields such as `patient`.
- **Portal bundle:** a Vite build with `target: es2015` and sourcemaps. Its assets are committed, so keep dependencies small.
- The codebase has no explicit caching layer (`frappe.cache` is rarely used).
