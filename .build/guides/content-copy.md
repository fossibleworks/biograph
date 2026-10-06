---
title: Content & copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/public/js/sales_invoice.js
  - healthcare/public/js/healthcare_practitioner.js
  - healthcare/permissions.py
  - patient_portal/src/components/Payment.vue
  - crowdin.yml
---

- **Tone**: plain, direct and instructional. Write in sentence case, often starting with "Please …" for required actions. Examples: "Please select a Patient to be invoiced", "Please Configure Clinical Procedure Consumable Item in {0}", "Only numbers are allowed in the phone number type field.", "You do not have permission to delete records."
- **Titles** name the category of problem: "Missing Configuration".
- **Terminology**: use the DocType names exactly, in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Healthcare Settings, Lab Test, Inpatient Record, Fee Validity, Insurance Payor. The product name is "Biograph". Clinical terms follow FHIR (Observation, Service Request, Diagnostic Report).
- **Placeholders**: positional `{0}`, filled with `.format()` (Python) or `__("… {0}", [x])` (JS). Link to the relevant record with `get_link_to_form`.
- **Translation**: every string must be translatable (`_()` / `__()`). Strings are collected into `healthcare/locale/main.pot` and translated through Crowdin.
- **Portal copy** is patient-friendly and short, e.g. "Pay Your Bill", "Details of fees", "One-time registration for new patients".
