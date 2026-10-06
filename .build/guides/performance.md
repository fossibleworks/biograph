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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
---

Hot or heavy paths inferred from the code:

- **Wildcard doc_events**: `"*"` on_submit, on_cancel and on_update_after_submit call Patient History Settings to create, delete or update Patient Medical Records. This runs on **every submitted document in the whole ERPNext site**, so keep it cheap and return early for doctypes it does not track.
- **Sales Invoice / Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) run inside ERPNext's accounting transactions.
- **Scheduler**:
  - `send_appointment_reminder` runs on the `all` tick, every few minutes.
  - Daily jobs scan appointments, fee validity, inpatient records and medication requests.
  - These need set-based queries, not per-row `get_doc` loops.
- **Appointment slot calculation**: `patient_appointment.py` is the largest controller, with availability, overlap and capacity checks. Portal booking and the desk calendar call it often.
- **Patient Portal API**: `get_appointments` and similar build multi-join `frappe.qb` queries. Select only the needed columns and filter by the patient set.
- **Indexes**: about 35 DocType JSONs set `"search_index": 1` (e.g. Clinical Procedure `patient`/`procedure_template`). Add `search_index` for new fields used in filters or joins.
- Very few background jobs (`frappe.enqueue`, about 2 uses) and no explicit caching (`frappe.cache`, 0 uses). Use `frappe.enqueue` for long bulk work instead of doing it inline in a request.
