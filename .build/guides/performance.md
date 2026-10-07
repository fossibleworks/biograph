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
  - patient_portal/src/socket.js
---

# Performance-sensitive areas

- **Wildcard doc_events:** `hooks.py` registers `on_submit`, `on_cancel` and `on_update_after_submit` on `*`, which create, update or delete Patient Medical Records. These run on **every submittable doctype in the whole ERPNext site**, so keep them cheap: return early when the doctype isn't configured in Patient History Settings.
- **Sales Invoice / Payment Entry hooks:** `manage_invoice_validate` and `manage_invoice_submit_cancel` sit on core accounting paths. Avoid per-row queries.
- **Scheduler:** `send_appointment_reminder` runs on **`all`**, every tick. The daily jobs (appointment status, fee validity, IP occupancy billing, medication-request expiry) scan large tables. Use filtered bulk queries.
- **Appointment scheduling:** slot availability, overlap and capacity checks in `patient_appointment.py` (an approximately 1900-line module, plus `recuring_appointment_handler.py`) and the block-based therapy booking. These back interactive calendar and portal requests.
- **Heavy work:** move it off the request with `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`, as recurring appointments and sample collection do.
- **Reports:** `healthcare/healthcare/report/*` (diagnosis trends, appointment analytics, medication item-wise sales). About 91 raw `frappe.db.sql` calls exist. Keep them parameterised and indexed, and prefer `frappe.qb` or `get_all` with fields and filters.
- **Portal:** whitelisted endpoints in `api/patient_portal.py`, and the portal uses cached frappe-ui resources (`getCachedListResource`).
