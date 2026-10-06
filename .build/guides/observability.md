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
  - patient_portal/src/socket.js
  - .github/workflows/codeql.yml
---

# Observability

There is no metrics or tracing stack (no OpenTelemetry, Sentry, or Prometheus in the repo). Observability relies on Frappe's built-in facilities:

- **Error Log doctype via `frappe.log_error`** (about 15 call sites) is the primary channel. Pass the traceback and a short, human-readable title, e.g. `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))` or `frappe.log_error(title="Error renaming DocType ...")`.
- **`frappe.logger()`** (a few call sites) is used for informational and error lines in patches and parsing fallbacks.
- **Audit trail:** Frappe document versioning and the Patient Medical Record timeline, which the wildcard doc_events populate.
- **Realtime:** `frappe.publish_realtime` is used sparingly. The portal has `socket.js`.
- **Coverage and security signals:** Codecov, CodeQL, Semgrep, pip-audit.

Use `frappe.log_error` for failures you swallow, and `frappe.logger()` for diagnostic info. Do not use `print()`. Never log PHI (patient-identifying clinical data) in error titles.
