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
  - healthcare/uninstall.py
  - patient_portal/src/socket.js
---

The project uses Frappe's built-in facilities only. It has no metrics or tracing libraries.

- **`frappe.log_error(message, title)`** is the primary error sink (about 15 uses). It writes to the Error Log doctype.
  - Pass `frappe.get_traceback()` or a descriptive message.
  - Use a short human title, e.g. "Appointment Confirmation Message Not Sent" or "Unavailability Calendar Event Error".
- **`frappe.logger().info/error(...)`** is used occasionally, mainly in patches, for file-based logs.
- **`print`** is acceptable only in install, uninstall, and migrate scripts (`uninstall.py`, `after_migrate.py`), which run in the bench console. Avoid `print` in request or controller code. Existing instances, such as in `patient_appointment.py`, are legacy.
- **`console.log`** appears about 23 times in JS. Don't add new ones to shipped code.
- **Realtime** updates use `frappe.publish_realtime` (rare). The portal uses a socket (`patient_portal/src/socket.js`) with frappe-ui cached resources.
- **CI-level:** Codecov coverage, CodeQL, semgrep, pip-audit.
