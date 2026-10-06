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
  - healthcare/healthcare/utils.py
  - healthcare/public/js/healthcare_practitioner.js
  - healthcare/locale/main.pot
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - README.md
---

- **Tone:** short and direct, in Title Case for labels and actions ("Create", "Schedule Admission", "Reason for Cancellation", "Change Item Code").
- **Messages:** errors are plain sentences, sometimes ending in "!" ("Patient already has an appointment booked for the same day!", "Appointment end must be after start."). Success notices name the record ("Sales Invoice {0} created", "Customer {0} is created.").
- **Throw titles:** short nouns ("Missing Configuration").
- **Terminology:** use the domain DocType names exactly as defined, in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Service Request, Observation, Diagnostic Report, Insurance Payor. The product is branded **Biograph**; patch `rebrand_marley_to_biograph` removed "Marley".
- **Translation:** every string goes through `_()` (Python) or `__()` (JS), with `{0}` placeholders, and is sent to Crowdin via `healthcare/locale/main.pot`.
- **Spelling:** the codebase uses British spelling in prose ("organisations"). The PR template follows ERPNext conventions.
