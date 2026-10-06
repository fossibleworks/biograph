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
  - healthcare/healthcare/utils.py
  - healthcare/public/js/mark_unavailable.js
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - healthcare/locale/main.pot
---

- **Always translatable:** wrap strings in `_()` in Python and `__()` in JS. Weekly POT generation and Crowdin pick them up. Use positional placeholders (`{0}`), not f-strings inside `_()`.
- **Tone:** short, direct, instructional sentences in Title-Case domain terms. Examples:
  - "Appointment Date and Time are required."
  - "Appointment end must be after start."
  - "Please Configure Clinical Procedure Consumable Item in {0}" (links the settings form)
  - "Patient already has an appointment booked for the same day!"
  - Alerts: "Checking for conflicts..."; dialog titles: "Mark Time as Unavailable"; actions: "Create", "OK".
- **Error titles** are short noun phrases: "Missing Configuration", "Appointment Confirmation Message Not Sent".
- **Terminology:** use the DocType names exactly as written. Patient, Healthcare Practitioner, Healthcare Service Unit, Medical Department, Patient Appointment, Patient Encounter, Inpatient Record, Lab Test, Observation, Diagnostic Report, Service Request, Medication Request, Fee Validity, Insurance Payor and Healthcare Settings are all capitalized as proper nouns.
- Product name: **Biograph** (a v16 patch rebranded "Marley" to Biograph). Do not introduce "Marley" in user-facing copy.
