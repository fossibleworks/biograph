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
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - patient_portal/src/socket.js
  - .pre-commit-config.yaml
---

There is no metrics or tracing library. Observability relies on Frappe's built-ins:
- **Error Log doctype:** `frappe.log_error(...)` (about 15 call sites), usually `frappe.log_error(frappe.get_traceback(), _("Human Title"))` or `frappe.log_error(title="...")`. Use it for failures in background, notification, calendar and patch code that should not block the user.
- **File logger:** `frappe.logger().info(...)` / `.error(...)`, used mainly in setup and patch code (`setup/patient_duplicate_check.py`, `patches/v15_0/setup_patient_duplicate_check_rules.py`) and for parse failures in appointment code.
- **User-visible feedback:** `frappe.msgprint` and realtime updates (`frappe.publish_realtime`, portal `socket.js`).
- Do not use bare `print()` or debug statements. Pre-commit's `debug-statements` hook rejects `pdb`/`breakpoint`.
- Background jobs started with `frappe.enqueue` appear in the RQ Job and Scheduled Job Log views in Desk.
