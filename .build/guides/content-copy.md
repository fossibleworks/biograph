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
  - patient_portal/src/components/Payment.vue
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Translatable always:** Python strings use `_()` and JS uses `__()`. Translations flow through `healthcare/locale/main.pot` and Crowdin. Portal Vue templates currently hard-code English strings.
- **Terminology** follows the domain models: *Patient*, *Healthcare Practitioner* (shown as "Practitioner"), *Patient Appointment*, *Patient Encounter*, *Service Unit*, *Medical Department*, *Lab Test*, *Observation*, *Diagnostic Report*, *Inpatient Record*, *Fee Validity*, *Therapy Session*. Use DocType names exactly and in Title Case.
- **Buttons and actions** are short Title Case verbs: "Create", "Add", "Submit", "Start", "Transfer", "Schedule Admission", "Schedule Discharge", "Book".
- **Errors** are short and direct, often sentence fragments, with the entity name in bold:
  - "Not allowed, cannot overlap appointment {0}"
  - "Appointment end must be after start."
  - "Patient already has an appointment booked for the same day!"
  - "Please select patient"
  - Dialog titles such as "Missing Configuration" or "Not Allowed".
- **Portal tone** is friendly and plain, with empty states like "Looks like you don't have any appointments yet." and "No Records Found". Headings include "Book an Appointment", "Pay Your Bill", "Select a Department" and "Select a Practitioner".
