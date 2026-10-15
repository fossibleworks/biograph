---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/www/patient_portal.py
  - patient_portal/src/socket.js
---

The app relies on Frappe's built-in facilities. There is no external metrics or tracing stack.

- **Error Log doctype:** `frappe.log_error(...)` is the main way failures are recorded (about 15 call sites). Always pass a descriptive `title`, e.g. `"Can't bill Service Unit occupancy"` or `"Unavailability Calendar Event Error"`, plus a message or `frappe.get_traceback()`.
- **Logger:** `frappe.logger()` is used for informational progress in setup and parsing code (about 9 calls), e.g. `frappe.logger().info("Starting patient duplicate check rules setup")`.
- **Telemetry:** `frappe.utils.telemetry.capture("active_site", "patient_portal")` runs when a logged-in user opens the portal.
- **Realtime:** the portal listens on socket.io for `refetch_resource` events to reload cached frappe-ui resources. The server side uses `frappe.publish_realtime`.
- **Frontend:** about 33 `console.log`/`console.error` calls exist across desk JS and the portal. Avoid adding more debug logging. The pre-commit `debug-statements` hook blocks Python debuggers.
