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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

# Performance-sensitive paths

- **Global `doc_events["*"]` hooks**: `on_submit`, `on_cancel` and `on_update_after_submit` of *every* doctype call `patient_history_settings.create/delete/update_medical_record`. Anything added there runs on every submit across ERPNext, so keep it cheap and return early for doctypes that are not tracked.
- **Appointment availability and booking**: `patient_appointment.py` (about 1900 lines) and `api/patient_portal.get_slots` compute practitioner slots, overlaps, capacity and unavailability on each request. Avoid per-slot DB queries and batch lookups instead.
- **Scheduler jobs**: `send_appointment_reminder` runs on `all` (every few minutes). The daily jobs (`update_appointment_status`, `update_validity_status`, `add_occupied_service_unit_in_ip_to_billables`, `update_expired_medication_requests`) scan whole tables, so filter with indexed fields and bulk updates.
- **Long-running work goes to the queue**: recurring appointment creation and sample collection processing use `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`. Follow this pattern for bulk operations instead of doing them inline in a request.
- **Portal order and result aggregation**: `api/patient_portal.get_orders` builds order maps from Service Requests, Invoices and nested Observations (`get_child_observations`). Watch for N+1 queries as patient history grows.
- **Invoice hooks**: `manage_invoice_validate` and `manage_invoice_submit_cancel` run on every Sales Invoice.
- **Reports** (`report/*`, such as patient appointment analytics and diagnosis trends) aggregate large date ranges. Prefer `frappe.qb` / SQL aggregation over Python loops.
- The portal SPA uses `getCachedResource` / `getCachedListResource` from frappe-ui to avoid repeat fetches.
