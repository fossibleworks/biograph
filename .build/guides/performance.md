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
---

These areas are likely to be performance-sensitive, based on the code's shape:

- **Wildcard `doc_events`** run on every submit, cancel, and update-after-submit for every DocType (Patient Medical Record creation via `patient_history_settings`). Keep that path cheap and exit early when a doctype isn't configured.
- **Sales Invoice hooks** (`manage_invoice_validate`, `manage_invoice_submit_cancel`) and the overridden `HealthcareSalesInvoice` run inside ERPNext billing. Avoid per-row queries in them.
- **Scheduler jobs:**
  - `send_appointment_reminder` runs on the `all` schedule, so it fires every few minutes. Query narrowly.
  - Daily jobs scan appointments, fee validity, inpatient occupancy billables, and expired medication requests.
  - Use `frappe.enqueue` for heavy work. It is barely used today, with only 2 calls.
- **Patient Portal APIs** (`api/patient_portal.py`) build multi-join `frappe.qb` queries per request. Prefer the query builder with explicit selects over N+1 `get_doc` loops.
- **Appointment scheduling:** availability and overlap checks in `patient_appointment.py`, `recuring_appointment_handler.py`, and block booking.
- **Reports and pages:** `patient_appointment_analytics`, `diagnosis_trends`, `lab_test_report`, `patient_history`, and `patient_progress` aggregate over large clinical tables.
- The `.pre-commit` and codecov configs have no perf budgets, and the repo has no caching layer: `frappe.cache` is unused.
