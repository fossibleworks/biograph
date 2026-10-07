---
title: Performance-sensitive paths
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
---

# Performance-sensitive paths

There is no explicit caching layer. No `frappe.cache`/`redis_cache` usage was found in the healthcare module. Hot paths rely on DB queries, so watch for N+1 queries and unindexed filters.

- **Global `doc_events["*"]`** (`on_submit`/`on_cancel`/`on_update_after_submit` → `patient_history_settings.create/delete/update_medical_record`) runs on **every submittable document in the whole site**, ERPNext included. Keep it cheap and return early when the doctype isn't configured.
- **Sales Invoice / Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`, insurance claim validation) are on the billing hot path.
- **Appointment scheduling**: `patient_appointment.py` (about 1,800+ lines) and portal `get_slots` compute availability and overlaps. They are called interactively.
- **Scheduler**: `send_appointment_reminder` runs on `all` (every tick). Daily jobs update appointment status, fee validity, inpatient billables and expired medication requests. All of these scan large tables, so batch them and filter by indexed fields.
- **Reports** (`healthcare/healthcare/report/*`: diagnosis_trends, patient_appointment_analytics, lab_test_report, etc.) aggregate over patient-scale datasets. Prefer `frappe.qb` with date filters.
- About 116 fields are marked `search_index: 1` in doctype JSON. Add indexes in the JSON when you introduce new frequent filters.
- The portal uses frappe-ui `createResource` / `getCachedResource` for client-side caching.
