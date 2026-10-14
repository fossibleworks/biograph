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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

# Performance-sensitive paths

- **Global doc_events on `*`:** `on_submit`, `on_cancel` and `on_update_after_submit` call `patient_history_settings` for *every* submitted doctype in the site, ERPNext documents included. Keep those handlers cheap and return early for doctypes that are not configured.
- **Sales Invoice and Payment Entry hooks:** `manage_invoice_validate`, `manage_invoice_submit_cancel` and `set_paid_amount_in_healthcare_docs` run on every invoice and payment. Avoid per-row queries inside them.
- **Appointment scheduling:** `patient_appointment.py` is about 1,900 lines. It covers availability and overlap checks, Practitioner Availability, unavailability and slot computation. The portal booking calendar calls it heavily. Use set-based `frappe.get_all`/`frappe.qb` queries filtered on date and practitioner, not loops of `get_doc`.
- **Schedulers:** `send_appointment_reminder` runs on the `all` (every-tick) scheduler. The daily jobs update appointment status, fee validity, inpatient billables and expired medication requests. Work in these jobs grows with history, so filter by date and status.
- **Portal APIs** (`api/patient_portal.py`): these build joined `frappe.qb` queries. Do not call `get_patients_with_relations()` twice per request, as `get_appointments` currently does.
- **Heavy work goes to the queue** with `frappe.enqueue`, e.g. recurring appointments and sample collection.
- **Patches** run over production data on migrate. Batch updates rather than loading every document.
- The repo has almost no explicit caching (`frappe.cache`). Measure before adding any.
