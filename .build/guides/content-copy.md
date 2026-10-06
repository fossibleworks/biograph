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
  - healthcare/public/js/healthcare_note.js
  - healthcare/public/js/form.js
  - healthcare/locale/main.pot
  - healthcare/patches.txt
---

- All copy is translatable: `_()` in Python and `__()` in JS. Strings are collected into `healthcare/locale/main.pot`.
- **Tone:** short, direct, sentence-case messages that end with a period, e.g. "Appointment Date and Time are required.", "Appointment end must be after start.". Errors may use "!" ("Patient already has an appointment booked for the same day!").
- Use `{0}` placeholders with `.format()` for record names, not f-strings inside `_()`.
- **Dialog actions** are single verbs: "Create", "Add", "Add Note", "Reject". Confirmations are phrased as questions ("Permanently Submit {0}?").
- **Terminology** follows the DocType names: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Observation, Service Request, Insurance Payor. "Practitioner" is preferred over "doctor". The product is "Biograph"; Marley was rebranded (`rebrand_marley_to_biograph` patch).
