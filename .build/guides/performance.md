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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/api/patient_portal.py
---

These paths are likely to be performance-sensitive. The list is inferred from the code's structure; there are no explicit perf budgets in the repo.

- **Appointment scheduling and slot availability**
  - `patient_appointment.py` is about 1,800+ lines. It covers overlap validation, practitioner unavailability, availability data and reminders.
  - It runs on every booking, both in desk and in the portal.
  - `send_appointment_reminder` runs on the `all` scheduler tick, which is every few minutes.
- **Wildcard doc_events**
  - `hooks.py` registers `on_submit`, `on_cancel` and `on_update_after_submit` for **every doctype** (`"*"`), to keep Patient Medical Record in sync.
  - Keep `patient_history_settings` handlers cheap, and return early for unrelated doctypes.
- **Billing hooks** run on every ERPNext Sales Invoice and Payment Entry validate, submit and cancel (`healthcare.healthcare.utils`, `custom_doctype/payment_entry.py`).
- **Daily scheduler jobs** sweep large tables: appointment status, fee validity, inpatient occupancy billables, expired medication requests.
- **Long work is queued**: `frappe.enqueue(..., queue="long", enqueue_after_commit=True)` handles recurring appointment creation and sample collection. Follow that pattern for bulk work.
- **Portal queries** (`api/patient_portal.py`) use `frappe.qb` joins across Appointment, Encounter, Practitioner, Patient and Company.
- **Indexes**: about 119 `search_index` flags in the doctype JSON. Upstream added more, for example on Clinical Procedure `patient` and `procedure_template`. Add `search_index` to fields used in hot filters.
- **Caching**: the healthcare code has no `frappe.cache` usage.
