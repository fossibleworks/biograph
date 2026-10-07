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
  - healthcare/public/js/healthcare_note.js
  - patient_portal/src/components/Payment.vue
  - healthcare/locale/main.pot
  - crowdin.yml
---

# Content / copy

- **Tone:** short, direct and clinical-administrative. Validation messages are plain statements:
  - "Appointment end must be after start."
  - "Registration Fee cannot be negative or zero"
  - "Start Date should be before End Date"
  - "Configure a service Item for {0}"
  
  A few use `!` for conflicts ("Patient already has an appointment booked for the same day!"); don't add more.
- **Titles:** Title Case ("Missing Configuration", "Not Available", "Add Clinical Note", "Create Service Request").
- **Buttons:** single verbs ("Add", "Done", "Create", "Book").
- **Terminology:**
  - Use Frappe DocType names verbatim and in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Fee Validity, Service Request, Medication Request, Observation, Diagnostic Report, Inpatient Record.
  - Write "Practitioner", not "Doctor", and "Service Unit", not "room".
- **Translation:**
  - Wrap every string in `_()` (Python) or `__()` (JS) with positional `{0}` placeholders. The strings feed `healthcare/locale/main.pot` and Crowdin (`crowdin.yml`).
  - Many portal Vue strings are still hard-coded English ("Details of fees", "Total", "Result", "Reference").
