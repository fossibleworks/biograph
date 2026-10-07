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
  - healthcare/public/js/sales_invoice.js
  - healthcare/locale/main.pot
  - crowdin.yml
  - healthcare/hooks.py
---

- **Every user-facing string is translatable**: `_()` in Python and `__()` in JS. Strings are extracted to `healthcare/locale/main.pot` and translated through Crowdin. Use positional placeholders (`{0}`, `{1}`) and call `.format()` *outside* `_()` so the template string stays stable.
- **Tone:** short, direct and neutral, in sentence case, usually ending with a period. Examples:
  - Validation: "Appointment Date and Time are required.", "Appointment end must be after start.", "Invalid Healthcare Service Unit", "Code Value is required"
  - Instructions: "Please select a Patient to be invoiced", "Please set a Customer linked to the Patient", "Please enter {}"
  - Rule violations: "Not allowed, cannot overlap appointment {}", "Not allowed, {} cannot exceed maximum capacity {}"
  - Confirmations: "Sales Invoice {0} created", "Appointment Cancelled."
  - Dialog titles in Title Case: "Missing Configuration", "Customer Not Found"
- **Terminology:** use the DocType names exactly, in Title Case (Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Lab Test, Clinical Procedure, Inpatient Record, Fee Validity, Service Request, Medication Request, Observation, Insurance Payor). Say "Practitioner", not doctor, and "Service Unit", not room or ward, in app copy. The product name in UI is **Biograph**.
- Avoid exclamation marks except where they already exist (e.g. "Patient already has an appointment booked for the same day!").
