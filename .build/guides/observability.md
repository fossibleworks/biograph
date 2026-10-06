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
  - .github/workflows/codeql.yml
---

The app has no metrics or tracing layer. Observability relies on Frappe built-ins:
- **`frappe.log_error(...)`** (about 15 sites) writes to the **Error Log** doctype. Use it for caught exceptions in side-effects, background jobs and patches. Pass the traceback (`frappe.get_traceback()`) plus a short translatable title, or use the `title=` kwarg.
- **`frappe.logger()`** (about 9 sites) handles informational and progress logging in setup and patches, e.g. `frappe.logger().info("Starting patient duplicate check rules setup")` and `.error(f"Could not parse appointment time: …")`.
- **`frappe.msgprint`** gives user-visible feedback. It is not logging.
- Leftover `print()` calls exist mainly in setup and patches. Don't add new ones in request paths.
- Realtime events (`frappe.publish_realtime`) and the portal socket (`patient_portal/src/socket.js`) push live updates.
- Security monitoring runs in CI: CodeQL (python, javascript), Semgrep, detect-secrets, pip-audit.
