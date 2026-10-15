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
  - healthcare/locale/main.pot
  - crowdin.yml
  - healthcare/patches.txt
---

**Tone:** short, direct, sentence-style statements in clinical/administrative language. Validation messages state the rule ("Appointment end must be after start.", "From Time must be before To Time"). Conflicts and duplicates sometimes end in `!` ("Patient already has an appointment booked for the same day!", "Cannot book time block appointment!").

**Buttons/actions** are Title Case verbs or nouns: "Reschedule", "Confirm", "Check In", "Make Payment", grouped under menus like "Status". Progress messages use an ellipsis: "Checking for conflicts...".

**Terminology** (use these exact DocType names in copy): Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Observation, Diagnostic Report, Service Request, Medication Request, Inpatient Record, Fee Validity, Insurance Payor, Healthcare Settings. The product name is **Biograph** (rebranded from Marley; see patch `rebrand_marley_to_biograph`).

**i18n:** every string is wrapped in `_()` / `__()`, extracted to `healthcare/locale/main.pot`, and translated through Crowdin. Don't build sentences by concatenating translated fragments when one translatable string with placeholders works.
