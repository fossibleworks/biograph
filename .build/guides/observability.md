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
  - .pre-commit-config.yaml
---

Biograph uses Frappe's built-in facilities only. There are no metrics or tracing libraries.

- **Error Log:** `frappe.log_error(message_or_traceback, "Short Title")` writes to the Error Log doctype. It is the main way to record failures from background jobs, patches and best-effort side effects (15 call sites). Include `frappe.get_traceback()` for exceptions.
- **App logger:** `frappe.logger().info/error(...)` is used sparingly, for example in patches.
- **Realtime and UI feedback:** use `frappe.publish_realtime` and `doc.notify_update()` to refresh clients. The portal listens for `refetch_resource` over socket.io.
- **Avoid:** about 38 non-patch `print()` calls (for example `DEBUG -`/`ERROR -` prints in `patient_appointment.py`) are legacy. Don't add more. Pre-commit's `debug-statements` hook blocks `pdb`/`breakpoint`.
- **CI-side:** Codecov coverage reports and CodeQL scanning.
