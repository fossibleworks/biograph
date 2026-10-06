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
  - healthcare/healthcare/doctype/patient_appointment/recuring_appointment_handler.py
  - healthcare/healthcare/doctype/sample_collection/sample_collection.py
  - patient_portal/src/socket.js
  - patient_portal/src/components/PractitionerSelector.vue
---

Paths that are likely to be performance-sensitive:

- **Scheduler jobs** in `hooks.py` scan large tables. `send_appointment_reminder` runs on *every* scheduler tick (`all`). The daily jobs are `update_appointment_status`, `update_validity_status`, `add_occupied_service_unit_in_ip_to_billables` and `update_expired_medication_requests`. Keep them set-based and indexed, and avoid loading documents one at a time in loops.
- **Appointment scheduling and availability** (`patient_appointment.py`, Practitioner Availability, recurring and block-based booking). Overlap and capacity checks run on every save, and slot lookups are called interactively from the desk and the portal.
- **Heavy work is already offloaded** with `frappe.enqueue` (recurring appointments, sample collection). Follow the same pattern for bulk operations.
- **Reports** (`patient_appointment_analytics`, `diagnosis_trends`, `lab_test_report`, …) aggregate over clinical history. Prefer `frappe.qb` or SQL aggregation over Python loops.
- **Patient portal API** (`api/patient_portal.py`) runs on every portal page load. The portal paginates practitioner lists and relies on socket `refetch_resource` events instead of polling.
- **Billing integration** with Sales Invoice runs per item. Watch for N+1 `get_doc` calls.
