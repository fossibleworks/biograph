---
title: Performance-sensitive areas
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
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
---

- **Global `doc_events['*']` hooks** (`patient_history_settings.create_medical_record`, `delete_`, `update_`) run on submit/cancel of **every** doctype. Keep them cheap, and return early for doctypes that don't apply.
- **Scheduler:** `send_appointment_reminder` runs on `all`, the most frequent tick. The daily jobs scan appointments, fee validity, inpatient records and medication requests. Use set-based queries and avoid loading full documents in loops.
- **Appointment slot and availability computation** (`patient_appointment.py`, about 1800+ lines: practitioner schedules, overlap and capacity checks, block booking) sits on the interactive booking path for both Desk and the portal.
- **Sales Invoice / Payment Entry hooks** (`manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`, insurance claim validation) add work to every ERPNext billing transaction.
- **Portal API:** `get_appointments` joins 5 tables and calls `get_patients_with_relations()` twice. Prefer one `frappe.qb` query with selected columns.
- **Background jobs:** heavy fan-out uses `frappe.enqueue` (recurring appointment creation, sample collection). Follow that pattern for bulk work.
- **Patches** on large tables (for example `populate_appointment_end_fields`) should batch their work and log failures instead of aborting.
- New doctype fields that are filtered on often get `search_index` (the upstream clinical_procedure sync added it on `patient`/`procedure_template`).
