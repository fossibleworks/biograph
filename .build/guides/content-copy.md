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
  - healthcare/healthcare/doctype/insurance_payor/insurance_payor.py
  - patient_portal/src/components/AppointmentModel.vue
  - healthcare/locale/main.pot
  - crowdin.yml
---

## Tone
Short, direct and administrative, written in sentence case. Messages usually end with a period, or with `!` for warnings that block an action.

Examples:
- "Appointment Date and Time are required."
- "Patient already has an appointment booked for the same day!"
- "Appointment Cancelled. Please review and cancel the invoice {0}"
- "Not allowed, cannot overlap appointment {}"

## Patterns
- Refuse an action with `Not allowed, ...`.
- Ask for missing input with `Please enter {}` or `Please set ...`.
- Name missing setup with `<Thing> Not Found` titles ("Practitioner Schedule Not Found", "Customer Not Found").
- Confirm success with `<Doc> {0} created`.
- Prefer `{0}` placeholders with `.format()` inside `_()`.

## Terminology
Use the DocType names exactly as written, in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Sales Invoice, Fee Validity, Inpatient Record, Service Request. The portal uses simple verbs such as "Book".

## Translation
All strings must be translatable (`_()` in Python, `__()` in JS) because a weekly POT regeneration feeds Crowdin. Avoid building sentences from concatenated fragments.
