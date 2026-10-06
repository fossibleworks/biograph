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
  - healthcare/healthcare/api/patient_portal.py
---

Likely hot or sensitive paths:
- **Appointment scheduling and availability.** `patient_appointment.py` is about 1.8k lines and covers slot computation, overlap and capacity checks, practitioner availability and recurring appointments. It runs on every booking, both in desk and in the portal.
- **The `doc_events` `"*"` hook** (on_submit/on_cancel → patient history medical records). It fires for *every* submitted doctype, so keep it cheap and return early for doctypes it does not care about.
- **`scheduler_events["all"]`** (`send_appointment_reminder`). It runs every few minutes, so its queries must be indexed and bounded.
- **Portal API** (`api/patient_portal.py`). It does multi-table `frappe.qb` joins over appointments, encounters and practitioners for a patient and their relations.
- **Reports** (`report/`: diagnosis trends, patient appointment analytics, and others), which aggregate over large tables.

Conventions already in use:
- Bulk or slow work goes through `frappe.enqueue(..., queue="long", is_async=True, enqueue_after_commit=True)` (recurring appointments, sample collection).
- Use `frappe.qb` with explicit fields rather than loading full docs in loops.
- Avoid N+1 `frappe.get_doc` calls inside loops.
