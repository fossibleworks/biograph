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
  - healthcare/healthcare/dashboard_chart_source/insurance_claim_status/insurance_claim_status.py
  - healthcare/healthcare/api/patient_portal.py
---

Inferred from the shape of the code:

- **`doc_events["*"]`** in `hooks.py` runs `patient_history_settings.create_medical_record` / `update_medical_record` / `delete_medical_record` on submit, cancel and update-after-submit of **every** DocType, including ERPNext ones. Keep these handlers cheap and exit early for doctypes that are not tracked.
- **The `all` scheduler** (every few minutes) runs `patient_appointment.send_appointment_reminder`, so it must not scan the whole appointment table. The daily jobs (`update_appointment_status`, `update_validity_status`, inpatient billables, expired medication requests) process large tables.
- **Appointment booking and availability:**
  - `patient_appointment.py` is large (about 1,800+ lines). It handles slot lookup (`get_availability_data`), overlap and capacity checks, and recurring and block booking.
  - Those functions run on each booking and on calendar views, so avoid N+1 `frappe.get_doc` calls inside loops.
- **Reports and dashboards:**
  - `healthcare/healthcare/report/*` covers patient appointment analytics, diagnosis trends, lab test report and others.
  - `dashboard_chart_source/*` aggregates across large tables with `frappe.qb`. Use `frappe.qb` aggregates and indexed filters.
  - Upstream added `search_index` on `patient` / `procedure_template` for this reason.
- **Patient Portal APIs** (`api/patient_portal.py`) are called by anonymous-facing users. Keep `get_all` field lists narrow. The portal caches with frappe-ui `getCachedListResource` / `getCachedResource`.
- There are about 171 raw SQL / query-builder call sites. Prefer `frappe.qb` with explicit fields over `select *`.
