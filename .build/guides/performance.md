---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

# Performance-sensitive areas

- **Appointment scheduling and availability**: `patient_appointment.py` is the largest controller (~1,900 lines). It handles slot computation, overlap and capacity checks, practitioner availability and recurring appointments. These paths run on every booking and from the portal. Keep queries bounded and indexed.
- **Scheduler jobs**: `send_appointment_reminder` runs on the `all` scheduler tick (every few minutes). Daily jobs update appointment status, fee validity, inpatient billables and expired medication requests. They scan whole tables, so filter in SQL and process in batches.
- **Wildcard doc_events**: `doc_events["*"]` (on_submit / on_cancel / on_update_after_submit → Patient Medical Record) fires for *every* submitted document site-wide, including ERPNext documents. Keep these handlers cheap and exit early.
- **Long-running work goes to the queue**: recurring appointment creation and sample collection use `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`. Follow that pattern rather than doing bulk work in a request.
- **Raw SQL**: about 90 `frappe.db.sql` call sites. Prefer `frappe.get_all` / the query builder with explicit `fields` and filters. Many doctype JSONs declare `search_index` on hot link fields; add one when you introduce a new frequently filtered field.
- **Reports and dashboard charts** (`report/`, `dashboard_chart_source/`) aggregate across appointments, encounters and lab tests, so they need date-bounded filters.
- **Portal**: a Vite SPA. Bundle size and the number of API round-trips to `api/patient_portal.py` matter on mobile.
