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
  - healthcare/public/js/sales_invoice.js
  - healthcare/healthcare/utils.py
  - crowdin.yml
  - healthcare/locale/main.pot
---

## Tone

Copy is short, direct and imperative. It uses sentence case and ends with a period or exclamation mark.

- Prompts: "Please select Healthcare Service", "Please enter {0}".
- Refusals start with "Not allowed, …": "Not allowed, cannot overlap appointment {}", "Not allowed, {} cannot exceed maximum capacity {}".
- Explanations name the record: "The practitioner {0} is not available during this time due to an unavailability record {1}", "Patient already has an appointment booked for the same day!".
- Escalations: "..., please contact System Manager".
- Error titles are Title Case nouns: "Missing Configuration", "Appointment Confirmation Message Not Sent".

## Terminology

Use the DocType names in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Healthcare Settings, Practitioner Availability. Say "Practitioner", not "Doctor".

## Translation

Wrap every user-facing string, in Python with `_()` and in JS with `__()`. Use positional placeholders through `.format()`. Avoid f-strings inside `_()` because the extractor can't capture them. One existing case in `patient_appointment.py` should not be copied. Strings are collected into `healthcare/locale/main.pot` and translated via Crowdin.
