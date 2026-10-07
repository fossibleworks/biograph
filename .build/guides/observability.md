---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - .pre-commit-config.yaml
---

# Observability

The app has no metrics or tracing; it relies on Frappe's built-in facilities:

- **`frappe.log_error(message, title)`** writes Error Log documents. It is the main mechanism (about 15 call sites), used for:
  - failed notifications or SMS
  - calendar-event errors
  - scheduler billing failures
  - patch failures
  
  Give each entry a short, specific title and include `frappe.get_traceback()` or the exception.
- **`frappe.logger().info/error(...)`** is used occasionally, in patches and for parse failures.
- **Background jobs** run through `frappe.enqueue` (RQ) and appear in RQ Job / Scheduled Job Log.
- **Desk dashboards** come from `dashboard_chart`, `dashboard_chart_source`, `number_card`, `healthcare_dashboard` and the per-doctype `*_dashboard.py`. These are product analytics, not ops telemetry.

Don't add `print()` (the `debug-statements` pre-commit hook guards against leftover debuggers) and don't add third-party telemetry SDKs.
