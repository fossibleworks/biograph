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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/api/patient_portal.py
---

Paths likely to be performance-sensitive:

- **Global `doc_events["*"]`:** on_submit, on_cancel and on_update_after_submit run `patient_history_settings` medical-record hooks for **every** submitted document on the site. Keep them cheap and return early for doctypes that are not tracked.
- **Sales Invoice and Payment Entry hooks:** `manage_invoice_validate` and `manage_invoice_submit_cancel` in `healthcare/healthcare/utils.py`, and the payment_entry hooks, run on core ERPNext billing flows.
- **Appointment scheduling:** `patient_appointment.py` is very large and computes slot availability, overlap and capacity checks and calendar events. Use indexed filters and avoid queries inside loops.
- **Scheduler:** `send_appointment_reminder` runs on `all` (every tick). Daily jobs update appointment status, fee validity, inpatient billables and expired medication requests.
- **Heavy work goes to the background:** use `frappe.enqueue`, as in sample_collection and the recurring appointment handler.
- **Portal API:** `api/patient_portal.py` uses single `frappe.qb` joins. Follow that pattern rather than per-row `get_doc`.
- **Indexes:** use `search_index` on hot link fields (for example clinical procedure `patient` and `procedure_template`).
- **Reports:** `report/` (patient_appointment_analytics, diagnosis_trends, …) scan large tables.
