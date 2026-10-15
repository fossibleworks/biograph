---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/hooks.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/dashboard_chart_source/service_unit_type_wise_admission_status/service_unit_type_wise_admission_status.py
---

# Performance-sensitive paths

- **Appointment scheduling** (`patient_appointment.py`, about 2.2k lines) is the hottest path. It covers `get_availability_data`, `get_available_slots`, `check_employee_wise_availability`, overlap and capacity checks, unavailability conflict checks, and block booking. These run on every booking dialog open and date change, from both Desk and the Patient Portal. Avoid per-slot or per-practitioner queries inside loops. Batch with `frappe.get_all` / `frappe.qb`.
- **Wildcard doc_events**: `hooks.py` registers `"*"` handlers for `on_submit`, `on_cancel` and `on_update_after_submit` (patient medical records). They run for *every* submitted doctype on the site, ERPNext's included, so they must stay cheap and exit early.
- **Sales Invoice / Payment Entry hooks** (`healthcare/healthcare/utils.py`, `custom_doctype/payment_entry.py`) run on every ERPNext invoice and payment validate/submit.
- **Scheduler jobs**: `send_appointment_reminder` runs on `all` (every few minutes). The daily jobs update appointment status, fee validity, inpatient occupancy billing and medication-request expiry, and can touch large tables. Bound the query set and consider `frappe.enqueue` for heavy work.
- **Patient Portal API** (`api/patient_portal.py`) is called for anonymous/website users. Keep the `get_all` field lists narrow.
- **Reports / dashboard chart sources** (`report/*`, `dashboard_chart_source/*`) aggregate over appointments, admissions and claims, and should use SQL/qb aggregation, not Python loops.
- About 105 raw `frappe.db.sql` calls exist. Check new ones for indexes on filter columns.
