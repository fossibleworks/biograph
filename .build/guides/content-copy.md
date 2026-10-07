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
  - healthcare/public/js/mark_unavailable.js
  - healthcare/public/js/form.js
  - healthcare/healthcare/doctype/patient_encounter/patient_encounter.js
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Translatable always:** wrap copy in `_()` in Python and `__()` in JS. Strings are extracted to `healthcare/locale/main.pot` and translated through Crowdin. Use `{0}` placeholders and never concatenate translated fragments, e.g. `__("Permanently Submit {0}?", [this.docname])`.
- **Tone:** plain, direct and clinical-administrative. Messages are short sentence-case statements ending in a period: "Appointment Date and Time are required.", "Appointment end must be after start.", "Not allowed to print this document." A few legacy messages end in "!", such as "Patient already has an appointment booked for the same day!". Prefer the period.
- **Prompts:** use imperative phrasing, e.g. "Please select Patient".
- **Labels and buttons:** Title Case nouns and verbs: "Create", "Mark Time as Unavailable", "Healthcare Practitioner", "Healthcare Service Unit", "From Time", "Reason for Unavailability".
- **Terminology:** use the DocType names exactly as the domain terms: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Inpatient Record, Lab Test, Clinical Procedure, Fee Validity, Insurance Payor. Say "Practitioner", not "Doctor", and "Service Unit", not "Room". The portal is called "Patient Portal".
