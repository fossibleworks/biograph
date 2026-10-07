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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/api/patient_portal.py
---

Paths likely to be performance-sensitive:

- **Wildcard doc_events.** `hooks.py` registers `"*"` on_submit/on_cancel/on_update_after_submit for Patient Medical Record history, so the hook runs on **every submittable document in the site**, including ERPNext ones. Keep it cheap and return early for doctypes that aren't configured.
- **Sales Invoice and Payment Entry hooks** run on every invoice and payment submit or cancel: `manage_invoice_submit_cancel`, `manage_invoice_validate` and the payment_entry handlers in `utils.py` / `custom_doctype/`.
- **Appointment scheduling.** `patient_appointment.py` is about 2.2k lines and covers slot availability, overlap and conflict checks, and block booking. The portal's `get_slots` / `make_appointment` and the Desk calendar call it often.
- **Scheduler jobs:** `send_appointment_reminder` runs on `all` (every tick). The daily jobs (appointment status, fee validity, inpatient billables, expired medication requests) iterate over large tables.
- **Reports** in `healthcare/healthcare/report/`, e.g. patient_appointment_analytics and diagnosis_trends, aggregate over large datasets.

Conventions: there are about 263 `frappe.db.get_value` calls and about 80 `frappe.qb` uses. Prefer a single `get_all` / `qb` query with `fields=[...]` over per-row `get_doc` in loops. Fetch only the fields you need. Long-running work goes through `frappe.enqueue`, which has only 2 uses so far. Avoid N+1 queries in loops over invoice items or appointments.
