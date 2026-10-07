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
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

# Content & copy

## Tone
- Plain, short and clinical-administrative.
- Error messages state the problem and often the reason, e.g.:
  - "Appointment end must be after start."
  - "Cannot Submit, not all samples are marked as 'Collected'."
  - "Patient Insurance Policy is required to create Insurance Coverage"
- Occasional exclamation for conflicts ("Patient already has an appointment booked for the same day!").

## Terminology and casing
- Use DocType names in **Title Case** exactly as defined: Patient Appointment, Healthcare Practitioner, Inpatient Record, Insurance Payor, Fee Validity, Healthcare Service Unit, Medical Department, Sales Invoice.
- Use "Practitioner" (not "doctor"), "Payor" (not "payer") and "Service Unit" (not "room"/"bed") to match the FHIR-flavoured model.
- Interpolate with `{0}`/`{1}` placeholders inside `_()` so strings stay translatable. Never build strings by concatenation. Wrap names in `frappe.bold()`.
- Error dialog titles are short noun phrases ("Missing Insurance Policy").

## Patient portal (patient-facing)
- Friendly, Title-Case headings and buttons: "Book an Appointment", "Available Slots", "Select a Department", "Select a Practitioner", "Pay Your Bill", "Payment Successful", "Consultation Fee".
- Empty states are conversational: "Looks like you don't have any appointments yet." and "No Records Found".

## Translation
All strings flow into `healthcare/locale/main.pot`, which Crowdin translates. Every new string must be wrapped in `_()` / `__()`.
