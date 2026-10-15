---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/medication_request/medication_request.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - .pre-commit-config.yaml
---

The project has no dedicated metrics or tracing. Observability relies on Frappe's built-in facilities:

- **Error Log doctype** through `frappe.log_error` (about 15 call sites). This is the main way to surface failures in background or best-effort code. Use `frappe.log_error(title="<what failed>: <doc name>", message=frappe.get_traceback())`.
- **`frappe.logger()`** (9 uses) for informational and progress logs in setup and patch code, for example `frappe.logger().info("Starting patient duplicate check rules setup")`.
- **Realtime** `frappe.publish_realtime` is used sparingly for UI progress.
- **JS:** `console.log` and `console.error` appear in Desk scripts (27 and 12). Do not add new `console.log` debug calls. ESLint's recommended set plus the pre-commit `debug-statements` hook (Python) guard against leftover debug code.
- **Coverage** reporting goes to Codecov from scheduled CI runs.
