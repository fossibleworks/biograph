---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/regional/india/abdm/utils.py
  - patient_portal/src/socket.js
  - .pre-commit-config.yaml
---

# Observability

There is no metrics or tracing stack. The project relies on Frappe's built-in facilities:

- **Error Log doctype** through `frappe.log_error(...)` (about 24 call sites). This is the primary channel. Give it a short `title`, a `message` containing the traceback (`frappe.get_traceback(with_context=True)`), and where possible `reference_doctype`/`reference_name` so the log links back to the record.
- **`frappe.logger()`** for informational or debug progress in setup and migration code (`setup/patient_duplicate_check.py` uses `.info`/`.debug`). It is rarely used elsewhere.
- **Integration audit records**: ABDM calls are persisted as `ABDM Request` documents with request, response, traceback and status. This is the pattern for auditing external API traffic.
- **Realtime**: the portal subscribes to socket.io (`patient_portal/src/socket.js`). Server code calls `doc.notify_update()` after background changes.
- Do not use `print()`. The pre-commit `debug-statements` hook blocks leftover debuggers.
