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
  - healthcare/locale/main.pot
  - crowdin.yml
---

## Terminology

Use the DocType names as written, in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Inpatient Record, Lab Test, Observation, Service Request, Insurance Payor, Healthcare Settings. Say "Practitioner", not "Doctor", in UI.

## Tone

Short, direct and declarative. Mostly sentence-like Title Case for labels and buttons, e.g. "Book an Appointment", "Select a Practitioner", "Pay Your Bill", "Add Observation", "Cancel Unavailability", "Check Conflicts".

## Error messages

State the rule plainly and include field names, e.g. "Appointment end must be after start.", "Start Date should be before End Date", "{0} is a holiday", "User {0} is disabled", "Configure a service Item for {0}". Put dynamic values in `{0}` placeholders and never concatenate them.

## Progress and empty states

Use a gerund with an ellipsis, e.g. "Checking for conflicts..." or "Creating unavailability record...". The empty state is "No Records Found". Confirmations ask a question, e.g. "Are you sure you want to cancel this unavailability record?"

## Translation

Wrap every string in `_()` or `__()`. Strings flow into `healthcare/locale/main.pot` and then to Crowdin.
