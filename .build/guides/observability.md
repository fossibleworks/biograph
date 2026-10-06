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
  - healthcare/healthcare/setup/patient_duplicate_check.py
  - .pre-commit-config.yaml
---

There is no metrics or tracing stack. Observability uses Frappe's built-in facilities:

- **Error Log doctype:** `frappe.log_error(frappe.get_traceback(), _("Short Title"))` or `frappe.log_error(title=...)` for caught failures in background jobs, notifications, calendar sync and patches (about 15 call sites). This is the main operational signal.
- **File logger:** `frappe.logger().info/error(...)` is used sparingly (about 9 sites, mostly setup and patches) for progress messages.
- **User feedback:** `frappe.msgprint`, plus `frappe.show_alert` on the client. Realtime events (`frappe.publish_realtime`) are used once.
- No `print()` debugging. pre-commit `debug-statements` blocks `pdb`/`breakpoint`.
- Background jobs run through `frappe.enqueue`, so their failures appear in RQ Job and Error Log.

New code should put a descriptive, translated title on `frappe.log_error` and keep the traceback.
