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
  - healthcare/healthcare/utils.py
  - crowdin.yml
---

# Content & copy

- **Terminology** follows DocType names in Title Case:
  - Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Lab Test, Observation, Service Request, Insurance Payor.
  - In messages, write "Practitioner", not "doctor", and "Service Unit", not "room".
  - Healthcare Settings is the configuration doc.
- **Errors** are short, plain sentences ending with a period (sometimes "!"). They state the problem or the fix. Examples:
  - "Appointment end must be after start."
  - "Configure a service Item for {0}"
  - "Patient already has an appointment booked for the same day!"
  - Titles: "Missing Configuration", "Not Available".
- **Desk actions** use Title Case verb phrases: "Add Observation", "Get Items From", "Get Items from Healthcare Services". Prompts read like "Please select a Patient to be invoiced".
- **Portal copy** uses Title Case headings and buttons: "Book an Appointment", "Available Slots", "Pay Your Bill", "Payment Successful". The empty state is "No Records Found".
- Every string must be translatable: `_()` in Python, `__()` in JS. Strings flow into `healthcare/locale/main.pot` and Crowdin. Use `{0}` placeholders instead of string concatenation.
