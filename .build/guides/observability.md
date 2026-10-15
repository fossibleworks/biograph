---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - patient_portal/src/socket.js
  - .github/workflows/codeql.yml
---

Observability relies on what Frappe provides. There is no metrics or tracing library.

- **`frappe.log_error(title=..., message=...)`** (about 15 call sites) writes to the **Error Log** DocType. This is the main way failures in background jobs, payment records, sample collection and medication requests become visible. Give it a short, descriptive `title` (for example `"Failed to mark Collected!"`) and pass the exception or traceback as `message`.
- **`frappe.logger()`** (about 9 call sites) writes to file-based site logs, at `.info` for setup progress (`setup/patient_duplicate_check.py`) and `.error` for parse failures.
- Some legacy code uses `print`. Do not add more, and use `frappe.logger()` instead. Pre-commit `debug-statements` blocks leftover debuggers.
- **Realtime:** `frappe.publish_realtime` is used sparingly. The portal consumes socket.io events through `patient_portal/src/socket.js`.
- **Audit trail:** Frappe document versioning and the healthcare **Patient Medical Record** (created through the wildcard doc_events) form the clinical activity history.
- **CI and security signals:** Codecov coverage, CodeQL (python and javascript), semgrep, pip-audit and detect-secrets.
