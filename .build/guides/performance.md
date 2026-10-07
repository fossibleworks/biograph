---
title: Performance
category: performance
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
---

The likely hot paths, judged from the shape of the code:

- **Appointment scheduling.** `patient_appointment.py` is about 1,900 lines. It computes availability and slots, checks overlap and capacity, handles recurring and block appointments (`recuring_appointment_handler.py`), and parses calendar events. The calendar views (`patient_appointment_calendar.js`) query it often.
- **Scheduler.** `send_appointment_reminder` is registered under `scheduler_events['all']`, so it runs on every scheduler tick and must stay cheap.
- **Wildcard doc events.** `doc_events['*']` on_submit/on_cancel run for **every** submitted document in the site, to create or delete medical records. Keep them short-circuiting.
- **Long work goes to the background.** `frappe.enqueue` is already used for bulk recurring appointments and sample collection. Follow that pattern for heavy work.
- **Reports.** These scan large tables: `report/` (patient_appointment_analytics, diagnosis_trends, lab_test_report, medication_item_wise_sales, inpatient_medication_orders) and the dashboard chart sources.
- **Patient portal.** The bundle is prebuilt and hashed, so keep `createResource` calls minimal.
