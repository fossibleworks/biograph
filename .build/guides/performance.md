---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/hooks.py
  - healthcare/healthcare/api/patient_portal.py
---

Likely hot paths:

- **Patient Appointment** (`patient_appointment.py`, roughly 1,800+ lines) handles slot availability, overlap and capacity checks, practitioner schedules, holidays, and fee validity on every booking and validate. Recurring and block appointments multiply this work, and `recuring_appointment_handler.py` already pushes it to `frappe.enqueue`.
- **Scheduler jobs:** `send_appointment_reminder` runs on `all` (every few minutes). Daily jobs cover appointment status, fee validity, inpatient billables, and expired medication requests. All of them scan large tables, so filter them in SQL.
- **Patient Portal API** (`api/patient_portal.py`) is public-facing and serves list endpoints through `frappe.db.get_all`. Always pass `fields`, filters, and limits.
- **Reports** (`report/` such as patient_appointment_analytics and diagnosis_trends) and dashboard chart sources aggregate over many records.
- The codebase contains about 91 raw `frappe.db.sql` calls. Prefer parameterised queries and indexed filters.

Conventions: move bulk or slow work (invoice and record creation for many rows, sample collection) to `frappe.enqueue`, use `frappe.db.get_value`/`get_all` with explicit fields over `frappe.get_doc` in loops, and avoid N+1 queries in validate hooks.
