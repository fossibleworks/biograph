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
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
---

Likely hot paths, based on the shape of the code:

- **Appointment scheduling and slot lookup:** `patient_appointment.py` (about 2.2k lines) handles availability, overlap and capacity checks. The portal endpoint `get_slots` calls it on every date change. Keep the per-slot DB queries bounded and avoid N+1 lookups over practitioner schedules.
- **Wildcard doc_events:** `hooks.py` registers `on_submit` / `on_cancel` / `on_update_after_submit` for **every** DocType (`"*"`) to maintain medical records through Patient History Settings. Anything added there runs on every submit across ERPNext. Keep it cheap and return early.
- **Billing hooks:** Sales Invoice validate/submit/cancel and Payment Entry hooks go through `healthcare/healthcare/utils.py` (about 1.9k lines), which updates healthcare docs on every invoice.
- **Scheduler:** `send_appointment_reminder` runs on `all` (every tick). The daily jobs update appointment, fee-validity and medication-request statuses and inpatient billables. Use set-based queries, not per-document loops.
- **Portal order aggregation:** `get_orders` / `get_data_from_service_requests` / `get_data_from_invoices` build nested maps across patients and observations.
- **Background work:** long tasks go through `frappe.enqueue` (recurring appointments, sample collection).
- **Indexes:** upstream adds `search_index` on link fields such as `patient` and `procedure_template` in DocType JSON. Do the same for new frequently filtered links.
