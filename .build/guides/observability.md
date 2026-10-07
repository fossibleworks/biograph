---
title: Observability
category: observability
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/patches/v15_0/setup_patient_duplicate_check_rules.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - healthcare/hooks.py
---

The app has no metrics or tracing of its own. It relies on Frappe's built-in facilities:
- **Error Log doctype:** `frappe.log_error(message, title)`, often with `frappe.get_traceback()`. Use this for failures in background jobs, patches and side effects.
- **Logger:** `frappe.logger().info/error(...)` writes to bench logs. Patches use it for setup progress.
- **Realtime:** `frappe.publish_realtime` sends progress and updates to the UI, for example in sample collection.
- **Background jobs:** `frappe.enqueue(..., queue="long", enqueue_after_commit=True)` jobs show up in RQ Job / Scheduled Job Log. Scheduled jobs are declared in `scheduler_events` in `hooks.py`.

There are about 24 `log_error`/`logger` call sites. Follow the same pattern, give each a short human-readable title, and do not log PHI in titles.
