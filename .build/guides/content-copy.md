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
  - healthcare/public/js/patient_quick_entry.js
  - patient_portal/src/components/Payment.vue
  - healthcare/locale/main.pot
  - crowdin.yml
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
---

- **Translatable:** every desk string goes through `_()` / `__()`. Strings are extracted to `healthcare/locale/main.pot` and synced with Crowdin (`crowdin.yml`).
- **Tone:** short and direct, in sentence form, ending with a full stop. Examples: "Appointment Date and Time are required.", "Appointment end must be after start.", "Only numbers are allowed in the Phone No field." An exclamation mark is sometimes used for conflicts ("Patient already has an appointment booked for the same day!").
- Highlight record names and practitioners with `frappe.bold()` and `{0}` placeholders.
- Dialog titles and labels use Title Case (`"Missing Configuration"`, `label: __('First Name')`).
- **Domain terminology** comes from FHIR and the doctypes: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Service Request, Observation, Diagnostic Report, Inpatient Record, Fee Validity, Insurance Payor. Use the exact DocType names.
- **Portal copy** speaks to the patient in the second person: "Pay Your Bill", "Consultation Fee", "One-time registration for new patients".
- Product name: **Biograph**. A v16 patch rebranded Marley to Biograph, so don't introduce "Marley" in user-facing text.
