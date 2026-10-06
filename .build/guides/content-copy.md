---
title: Content and copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/healthcare/utils.py
  - crowdin.yml
---

- **Always translatable:** wrap strings in `_()` (Python) or `__()` (desk JS). Crowdin and `locale/main.pot` pick them up. Use positional placeholders and `.format()`, not f-strings inside `_()`.
- **Tone:** short, direct, and in sentence case for messages, e.g. "Appointment Date and Time are required.", "Please set a Customer linked to the Patient", "Patient already has an appointment booked for the same day!". Refusals often start with "Not allowed, …".
- **Buttons and titles** use Title Case verbs and nouns: "Reschedule", "Confirm", "Check In", "Make Payment", "Book an Appointment", "Book". Error dialog titles are noun phrases: "Missing Configuration", "Invalid Healthcare Service Unit".
- **Empty states** are plain statements: "No slots available".
- **Domain terms** follow the DocType names: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Inpatient Record, Fee Validity.
