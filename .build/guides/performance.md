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
  - healthcare/healthcare/api/patient_portal.py
---

Paths that are likely performance-sensitive:

- **Global `doc_events` on `"*"`:** `patient_history_settings.create/delete/update_medical_record` runs on submit, cancel and update-after-submit of *every* doctype. Keep these handlers cheap and return early for doctypes that aren't relevant.
- **Sales Invoice and Payment Entry hooks** (`utils.manage_invoice_submit_cancel`, `manage_invoice_validate`, `payment_entry.*`, insurance claim validation) sit in ERPNext's billing hot path.
- **Scheduler:** `send_appointment_reminder` runs on the `all` event (every few minutes). Daily jobs scan appointments, fee validity, inpatient records and medication requests. Use set-based queries in these jobs, not per-row `get_doc` loops.
- **Appointment booking:** slot availability, overlap and capacity checks, and practitioner unavailability in `patient_appointment.py` (about 1,900 lines) are called interactively from Desk and the portal.
- **Portal API** (`api/patient_portal.py`): uses multi-join `frappe.qb` queries per patient and their relations.
- **Heavy work goes to the background:** recurring appointment creation and sample collection already use `frappe.enqueue(..., queue="long", enqueue_after_commit=True)`. Follow that for bulk operations.
- **Reports** in `healthcare/healthcare/report/` (analytics and trends) aggregate over large tables.
- Prefer `frappe.qb`/`frappe.db.get_all` with explicit `fields` and filters over loading full documents. Avoid N+1 `frappe.get_doc` inside loops.
