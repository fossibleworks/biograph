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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - patient_portal/vite.config.js
---

# Performance-sensitive areas

- **Appointment scheduling and slot availability** (`patient_appointment.py`, about 1,900+ lines). It computes availability, overlaps, capacity, holidays and recurring appointments, and the portal calls it for slot lists. Avoid per-slot DB queries. Batch with `frappe.get_all` and filters.
- **Scheduler jobs** in `hooks.py`:
  - `send_appointment_reminder` runs on **every** scheduler tick (`all`).
  - Daily jobs scan appointments, fee validity, inpatient records (occupancy billables) and medication requests.
  - These jobs must stay cheap and use indexed filters.
- **Bulk operations**, such as recurring appointment creation and sample collection, already go through `frappe.enqueue`. Push new long-running work to background jobs too.
- **Billing paths**: Sales Invoice / Payment Entry overrides and `get_healthcare_services_to_invoice` run on every invoice.
- **Reports and dashboards**: `report/` (appointment analytics, diagnosis trends, lab test report) and `dashboard_chart_source/` aggregate over large tables. Prefer SQL aggregation (`frappe.qb`/`frappe.db.sql`) over Python loops.
- **Patient Portal bundle**: Vite build targets es2015 with sourcemaps. Keep dependencies lean.
- There are about 318 raw `frappe.db.sql` / `get_all` / `get_list` call sites. Watch for N+1 queries inside loops.
