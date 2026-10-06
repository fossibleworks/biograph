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
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - .pre-commit-config.yaml
  - .github/workflows/codeql.yml
---

There is no metrics or tracing stack. Observability relies on Frappe built-ins:

- **Error Log doctype** through `frappe.log_error(title=..., message=...)`, with about 15 sites. This is the main way to record unexpected failures in hooks, patches and integrations. Use a short, specific title, e.g. `"Unavailability Calendar Event Error"`, and include the traceback (`frappe.get_traceback()`) or the exception as the message.
- **`frappe.logger()`**: about 9 sites, used for informational/error lines in patches and parsing code, e.g. `frappe.logger().error(f"Could not parse appointment time: {appt_time_str}")`.
- **Integration request logs**: ABDM calls are recorded in the `ABDM Request` doctype.
- **Avoid `print()`**: about 39 remain, mostly in patches/setup. The `debug-statements` pre-commit hook blocks `pdb`/`breakpoint`.
- CI captures bench logs (`bench_run_logs.txt`). Coverage goes to Codecov. CodeQL runs weekly and on PRs to `develop`.
