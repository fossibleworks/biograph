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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
---

Observability relies on Frappe's built-in facilities. There is no external metrics or tracing integration.

- **Error Log:** use `frappe.log_error(...)` (about 24 logging call sites). It writes to the Error Log doctype. Pass a short, descriptive **title** and a traceback **message**:
  - `frappe.log_error(title=f"Medication Request expiry update failed: {request.name}", message=frappe.get_traceback())`
  - `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`
- **Logger:** `frappe.logger().info(...)` / `.error(...)` is used rarely, for setup progress and parse failures (`setup/patient_duplicate_check.py`, `patient_appointment.py`).
- **Request/integration logs:** ABDM calls are persisted as `ABDM Request` documents. Payments are recorded in `Healthcare Payment Record`.
- **Desk dashboards:** `dashboard_chart`, `dashboard_chart_source` (department-wise appointments, insurance claim status, admission status) and `number_card` are product analytics, not ops monitoring.
- **Avoid:** `print()` for diagnostics (about 75 non-test prints exist, mostly legacy) and `console.log` left in JS. Prefer `frappe.log_error` / `frappe.logger()`.
