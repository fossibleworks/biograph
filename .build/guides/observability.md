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
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - healthcare/www/patient_portal.py
  - patient_portal/src/socket.js
---

# Observability

There is no dedicated metrics or tracing stack. The app relies on Frappe built-ins:

- **Error Log DocType** via `frappe.log_error(message, title)`. This is the main channel for failures in scheduled jobs, notifications, patches and external API calls (about 15 call sites). Give each one a short, specific `title` ("Unavailability Calendar Event Error", "Cant complete API call").
- **App logger** via `frappe.logger().info/debug/error(...)` for progress messages in setup routines (`healthcare/healthcare/setup/patient_duplicate_check.py`) and parsing problems.
- **Product telemetry:** `frappe.utils.telemetry.capture("active_site", "patient_portal")` when a logged-in user loads the portal.
- **Realtime:** the portal opens a socket (`patient_portal/src/socket.js`) for live updates.
- Don't commit stray `print()` calls in non-test code. Use `frappe.logger()` instead.
