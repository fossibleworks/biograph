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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - patient_portal/vite.config.js
---

Likely hot paths, based on how the code is wired:

- **Wildcard doc events:** `hooks.py` registers `doc_events["*"]` `on_submit`, `on_cancel` and `on_update_after_submit` handlers that create, update or delete Patient Medical Records. These run on **every submittable document in the site**, including all ERPNext ones. Keep them cheap and exit early.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, submit/cancel, `set_paid_amount_in_healthcare_docs`) run on every invoice and payment. Avoid N+1 queries there.
- **Scheduler:** `send_appointment_reminder` runs on the `all` schedule, every few minutes. Daily jobs update appointment, fee validity and medication-request statuses, and inpatient billables. These scan large tables, so filter in SQL.
- **Appointment booking and slots:** slot and availability calculations, overlap checks, and recurring appointments in `patient_appointment.py` (very large) are used interactively by desk and the portal.
- **Heavy work goes to the queue:** use `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`, as recurring appointments and sample collection already do.
- **Queries:** prefer `frappe.get_all(..., fields=[...], pluck=...)` and `frappe.qb` over loading full docs in loops (about 160 get_all/get_list uses).
- **Portal bundle:** Vite builds to an es2015 target with sourcemaps. Keep frappe-ui imports tree-shakeable.
