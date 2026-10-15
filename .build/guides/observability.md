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
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - patient_portal/src/socket.js
  - .pre-commit-config.yaml
  - .github/workflows/codeql.yml
---

Observability relies on Frappe's built-in facilities. The repo has no external metrics or tracing SDKs.

- **Error Log doctype** (`frappe.log_error`, 15 call sites) is the main signal. Use it for caught failures in background or side-effect code. Give it a descriptive `title`, the traceback (`frappe.get_traceback(with_context=True)`), and `reference_doctype` / `reference_name` so the entry links to the record.
- **`frappe.logger()`** (9 call sites) is used for informational setup and progress logging. Examples are `frappe.logger().info("Starting patient duplicate check rules setup")` and `.error(...)` for parse failures. Use it when the event is not something an admin needs to act on.
- **Realtime and UI feedback**: `doc.notify_update()` and `frappe.publish_realtime` push changes to open forms and the portal (`patient_portal/src/socket.js`).
- **Document timeline**: Frappe versioning and comments record status changes. Status fields (appointment status, fee validity status) are updated by scheduler jobs.
- **Avoid `print()`** in non-test code. There are roughly 70 leftover prints under `doctype/`. Pre-commit's `debug-statements` hook blocks `pdb`/`breakpoint`.
- CI captures coverage and uploads it to Codecov on nightly runs. CodeQL runs weekly and on develop.
