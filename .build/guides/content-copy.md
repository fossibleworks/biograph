---
title: Content and copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/locale/main.pot
  - crowdin.yml
  - healthcare/patches.txt
---

- **All copy is translatable:** `_()` in Python and `__()` in JS and templates. Strings are collected into `healthcare/locale/main.pot`, and Crowdin is configured.
- **Tone:** short, direct, clinical and operational. Use title-case button labels: "Reschedule", "Check In", "Make Payment", "Confirm" (grouped under "Status"). Use title-case field names in messages: "Appointment Date and Time are required.", "From Time must be before To Time".
- **Errors:** state the rule or problem plainly, sometimes with an exclamation for conflicts ("Patient already has an appointment booked for the same day!"). Add a remedy for configuration problems ("SMS not sent, please check SMS Settings").
- **Progress messages** end with an ellipsis ("Checking for conflicts...").
- **Domain terms:** Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Observation, Diagnostic Report, Service Request, Fee Validity, Insurance Payor. Use DocType names exactly as defined.
- **Branding:** "Biograph" (the `rebrand_marley_to_biograph` patch renamed it from Marley). Don't introduce "Marley" in user-facing copy.
