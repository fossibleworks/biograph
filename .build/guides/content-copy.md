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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/src/components/BookAppointmentModel.vue
  - crowdin.yml
---

- **Tone:** short, direct and clinical-administrative. Sentences end with a period, and some warnings end with "!". Examples: "Appointment Date and Time are required.", "Appointment end must be after start.", "Patient already has an appointment booked for the same day!"
- **Buttons and actions** use Title Case verbs: "Reschedule", "Confirm", "Check In", "Make Payment". Grouped buttons go under a Title Case group such as "Status".
- **Empty states (portal):** "No Records Found", "No slots available".
- **Error-log titles** are Title Case noun phrases: "Appointment Confirmation Message Not Sent", "Unavailability Calendar Event Error".
- **Terminology:** use the DocType names exactly as defined: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Insurance Payor, Observation, Service Request. Say "Practitioner", not "Doctor".
- **Translation:** all desk strings go through `_()` / `__()`. They end up in `healthcare/locale/main.pot` and are translated through Crowdin. Portal strings are currently hard-coded English.
