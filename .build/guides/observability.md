---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - .pre-commit-config.yaml
---

Biograph relies entirely on **Frappe's built-in facilities**. It has no external metrics or tracing (no Sentry/OpenTelemetry/statsd in the app).

- **`frappe.log_error(message, title)`** is the main failure record. It creates an *Error Log* document visible in Desk. It is used in about 15 places, usually with `frappe.get_traceback()` as the message and a short human title such as `"Appointment Confirmation Message Not Sent"` or `"Populate Appointment End Fields Patch"`. Prefer the keyword form `frappe.log_error(title=..., message=...)` for clarity.
- **`frappe.logger()`** (`.info` / `.error`) writes to bench log files. It is used sparingly in setup and patches (`healthcare/setup/patient_duplicate_check.py`) and for parse failures. There are about 9 calls and no `logging.getLogger`.
- **User-visible signals:** `frappe.msgprint(..., indicator="orange")` or `alert=True` for soft failures and confirmations.
- **Realtime:** `frappe.publish_realtime` pushes UI updates, e.g. after sample collection.
- **Audit trail:** Frappe document versioning, plus Patient Medical Record entries created by the wildcard `doc_events` hooks (`patient_history_settings`).
- Do not add `print()` debugging. pre-commit's `debug-statements` hook rejects `pdb`/`breakpoint`.
