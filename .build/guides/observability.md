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
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/healthcare_payment_record/healthcare_payment_record.py
  - eslint.config.mjs
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

# Observability

There is no dedicated metrics or tracing stack. Observability relies on Frappe built-ins:

- **Error Log doctype** through `frappe.log_error(message, title)`, used about 15 times for failures in background or side-effect paths (notifications, calendar events, payment records, medication request expiry, IP occupancy billing). Include `frappe.get_traceback()` or the exception, plus a human-readable title.
- **The Frappe logger** through `frappe.logger().info/debug/error(...)`, used mainly in setup and patches (`setup/patient_duplicate_check.py`, `patches/v15_0/setup_patient_duplicate_check_rules.py`) and for parse failures in `patient_appointment.py`.
- The Python `logging` module is not used directly, and `print` is not used for diagnostics.
- **Desk JS**: ESLint warns on `console.*` (`no-console: warn`), so do not leave console logging in committed code.
- **Realtime**: `frappe.publish_realtime` (for example in `sample_collection.py`) and Socket.IO on the portal push UI updates. These are not telemetry.
- Coverage reporting goes to Codecov from scheduled CI runs.
