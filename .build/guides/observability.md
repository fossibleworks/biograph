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
  - healthcare/patches/v16_0/rename_time_block_to_practitioner_availability.py
  - healthcare/regional/india/abdm/utils.py
  - healthcare/healthcare/doctype/abdm_request/abdm_request.py
  - healthcare/hooks.py
---

The app uses Frappe's built-in facilities and adds no external metrics or tracing stack.

- **Error Log:** `frappe.log_error(...)` is the main mechanism (about 15 call sites). It writes an *Error Log* record viewable in Desk. Pass the traceback and a short human title: `frappe.log_error(frappe.get_traceback(), _("Appointment Confirmation Message Not Sent"))`. Newer code uses the keyword form `frappe.log_error(title="...")`.
- **Structured app logs:** `frappe.logger(...)` appears in a handful of places (about 9). Use it for informational or debug traces instead of `print`.
- **Integration audit trail:** each ABDM call is persisted as an **`ABDM Request`** doc holding the request payload, URL, request name and response. Mirror this request-log-doctype pattern for new external integrations.
- **Domain audit:** submit, cancel and update events feed the **Patient Medical Record** timeline through `patient_history_settings`. Frappe's document versioning and timeline cover user actions.
- **CI-side:** Codecov coverage, CodeQL and semgrep findings.
- **Anti-pattern present:** `patient_appointment.py` uses `print(f"DEBUG - ...")` / `print(f"ERROR - ...")` (about 71 `print(` calls across doctype modules). These go to worker stdout only. Do not add more; convert them when you touch that code.
