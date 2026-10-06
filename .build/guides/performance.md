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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

Likely hot or heavy paths:
- **The `*` doc_events wildcard** (`patient_history_settings.create/delete/update_medical_record`) runs on submit, cancel and update-after-submit of *every* doctype. Keep it cheap and return early.
- **Sales Invoice and Payment Entry hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`, `set_paid_amount_in_healthcare_docs`) sit in ERPNext's billing path.
- **Scheduler:** `send_appointment_reminder` runs on `all` (every tick). The daily jobs scan appointments, fee validity, inpatient records and medication requests. Use filtered `frappe.get_all` and batch the work.
- **Appointment slot and availability logic** in `patient_appointment.py` (overlap checks, practitioner availability) is called interactively from the calendar and the portal.
- **Portal APIs** (`api/patient_portal.py`) use `frappe.qb` joins across Appointment, Encounter, Practitioner, Patient and Company. Prefer single joined queries over per-row `get_doc`.
- **Reports** (`report/`, e.g. `patient_appointment_analytics`, `diagnosis_trends`) aggregate over large tables.
- Long-running work uses `frappe.enqueue` (recurring appointments, sample collection).
- DocType JSON adds `search_index` on frequently filtered link fields (for example `patient`), as upstream did.
