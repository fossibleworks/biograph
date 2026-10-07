---
title: Content & Copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - patient_portal/src/components/Payment.vue
  - crowdin.yml
---

- **Translation:** wrap every string with `_()` in Python and `__()` in desk JS. Strings flow into `healthcare/locale/main.pot` and then into Crowdin. Use `{0}` placeholders with `.format()` instead of concatenating text into translated strings.
- **Tone:** short, direct, sentence-style messages, sometimes ending in `!`. Examples: "Patient already has an appointment booked for the same day!", "Appointment end must be after start.", "Code Value is required". Error titles are short Title Case nouns: "Missing Configuration", "Customer Not Found", "Not Available".
- **Buttons:** Title Case verbs: "Check In", "Reschedule", "Make Payment", "Repeat Appointments", "Mark Unavailable". Related actions are grouped under a menu such as `__("Status")`.
- **Terminology:** use the doctype names exactly: Patient Appointment, Patient Encounter, Healthcare Practitioner, Healthcare Service Unit, Medical Department, Inpatient Record, Fee Validity, Insurance Payor.
- **Portal copy** is friendlier and patient-facing: "Pay Your Bill", "Consultation Fee", "One-time registration for new patients".
