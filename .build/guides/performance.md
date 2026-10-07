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
  - healthcare/controllers/queries.py
  - healthcare/patches/v16_0/populate_appointment_end_fields.py
---

Likely hot or heavy paths, inferred from the code's shape:

- **Patient Appointment** (`patient_appointment.py`, roughly 1,900+ lines) handles availability and slot calculation, overlap and capacity checks, calendar events, and invoicing. It is called interactively from the booking UI and the portal. Watch for per-slot queries inside loops, and prefer batched `frappe.get_all` with filters and fields.
- **Scheduler jobs:** `send_appointment_reminder` runs on the `all` tick (every few minutes). Daily jobs cover appointment status, fee validity, inpatient billables, and expired medication requests. They scan tables that grow over time, so keep them filter-indexed and idempotent.
- **Wildcard `doc_events["*"]`** runs Patient Medical Record creation, update, and delete on submit, cancel, and update-after-submit of **every** document. Keep it a cheap early-exit when the doctype is not configured in Patient History Settings.
- **Sales Invoice / Payment Entry hooks** run on every ERPNext invoice and payment, healthcare or not, and must short-circuit quickly.
- **Reports** (`healthcare/healthcare/report/*`: appointment analytics, diagnosis trends, lab test report, medication sales) aggregate over large date ranges. Use `frappe.qb` or SQL aggregation, not Python loops.
- **Raw SQL** (~90 `frappe.db.sql` calls) and `standard_queries` link-search queries (`healthcare/controllers/queries.py`) run on every keystroke in link fields.
- **Patient Portal** bundle: built assets are committed. Keep dependencies lean.
- Patches that iterate all records (e.g. `populate_appointment_end_fields`) should batch commits on large sites.
