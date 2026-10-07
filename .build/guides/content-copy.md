---
title: Content & copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient/patient.js
  - healthcare/locale/main.pot
---

- **Tone:** direct, short and operational, written for clinical and admin staff. Sentences usually end with a period, and an exclamation mark appears only on hard conflicts (`'Patient already has an appointment booked for the same day!'`).
- **Patterns:**
  - Blocking rules start with `'Not allowed, ...'`, for example `'Not allowed, cannot overlap appointment {}'`.
  - Prompts take the form `'Please enter {}'`.
  - Required fields: `'Appointment Date and Time are required.'`.
  - Configuration gaps use the title `'Missing Configuration'`.
  - Escalation: `'..., please contact System Manager'`.
- Interpolate record names and values with `.format()` and wrap them in `frappe.bold()`. Always wrap strings in `_()` / `__()` so they reach `locale/main.pot`.
- **Terminology** (use the DocType names exactly, in Title Case): Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Inpatient Record, Lab Test, Observation, Service Unit, Medical Department, Therapy Plan, Fee Validity, Service Request. The product name is **Biograph**.
- Portal button labels are short verbs (`'Book'`).
