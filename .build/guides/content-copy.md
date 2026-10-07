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
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/Payment.vue
  - healthcare/locale/main.pot
  - crowdin.yml
---

# Content and copy

- **Tone:** plain and clinical-administrative, in sentence-style messages. Use "Please ..." for required actions: "Please set a Customer linked to the Patient", "Please enter {0}".
- **Constraint messages** follow the pattern "Not allowed, ...": "Not allowed, cannot overlap appointment {}". Facts are stated directly: "Patient already has an appointment booked for the same day!", "Appointment end must be after start."
- **Dialog titles** are short Title Case nouns: "Missing Configuration", "Customer Not Found", "Invalid Healthcare Service Unit", "Practitioner Schedule Not Found".
- **Success alerts** are short past-tense statements: "Sales Invoice {0} created", "Appointment Cancelled."
- **Terminology** matches the DocType names exactly, in capitalised form: Patient, Healthcare Practitioner, Healthcare Service Unit, Medical Department, Fee Validity, Service Request, Lab Test. Write "Practitioner", not "doctor", in system copy.
- **Portal copy** is friendlier and patient-facing: "Pay Your Bill", "Consultation Fee", "One-time registration for new patients".
- All strings must be translatable (`_()` / `__()`). They feed `healthcare/locale/main.pot` and Crowdin.
