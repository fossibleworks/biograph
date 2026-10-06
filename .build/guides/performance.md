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
  - healthcare/healthcare/api/patient_portal.py
---

Likely hot or heavy paths:

- **Wildcard doc_events:** `hooks.py` registers `on_submit`, `on_cancel` and `on_update_after_submit` for **every doctype (`*`)** to create, update or delete medical records (`patient_history_settings`). These run on every submit in the whole ERPNext site, so keep them cheap and exit early when the doctype isn't configured.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, payment-entry handlers, insurance-claim validation) sit on core accounting paths.
- **Scheduler:** `send_appointment_reminder` runs on `all` (every few minutes). The daily jobs (`update_appointment_status`, fee validity, inpatient billables, expired medication requests) scan large tables, so use filtered `get_all` / `frappe.qb` and batch updates.
- **Appointment availability and slot computation** in `patient_appointment.py` checks overlaps, capacity, practitioner schedules and unavailability for each booking request. Booking is also exposed to the portal.
- **Portal API** (`api/patient_portal.py`) uses `frappe.qb` joins across Appointment, Encounter, Practitioner and Patient.
- **Background work:** long operations already use `frappe.enqueue` (recurring appointments, sample collection). Follow that pattern rather than doing heavy work in a request.
- **Reports** (`report/`: patient_appointment_analytics, diagnosis_trends, lab_test_report, ...) aggregate over large clinical datasets.
- Avoid N+1 `frappe.get_doc` calls in loops. Fetch only the fields you need with `get_all(fields=...)` or `get_value`.
