---
title: Content & copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/locale/main.pot
  - crowdin.yml
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/public/js/sales_invoice.js
  - healthcare/patches.txt
---

- **Every user-facing string is translatable.** Use `_()` in Python and `__()` in JS and Jinja templates. Strings are extracted into `healthcare/locale/main.pot` and translated through Crowdin. Use positional placeholders inside the translated string: `_("Invalid Code Value: {0}").format(code_value)`. Do not concatenate strings or call `.format()` inside `_()`. The existing `_("{0} is a holiday".format(date))` is an anti-pattern.
- **Tone:** short, plain, sentence-case statements of the problem, e.g. "Appointment Date and Time are required.", "Appointment end must be after start.", "Please select Healthcare Service", "Patient already has an appointment booked for the same day!". Error dialogs get a Title Case title (`"Missing Configuration"`, `"Not Available"`).
- **Buttons and dialog titles** use Title Case verb + noun: "Add Observation", "Edit Observation", "New Service Request", "New Medication Request".
- **Terminology:** use the DocType names exactly as defined: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Observation, Service Request, Medication Request, Inpatient Record, Fee Validity, Insurance Payor. The product brand is **Biograph**. Patch `v16_0.rebrand_marley_to_biograph` removed "Marley" from user-facing text, so do not reintroduce it.
