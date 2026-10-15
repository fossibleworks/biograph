---
title: Content & copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/public/js/mark_unavailable.js
  - healthcare/healthcare/doctype/healthcare_settings/healthcare_settings.py
  - healthcare/healthcare/doctype/lab_test/lab_test.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - healthcare/locale/main.pot
---

- **Tone:** short, direct and operational, written for clinical and billing staff. Use Title Case for labels and buttons ("Add Observation", "Get Items From", "Book an Appointment"). Use sentence case for messages ("Please select a Patient to be invoiced", "Registration Fee cannot be negative or zero").
- **Terminology:** capitalise DocType names when referring to records: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Service Unit, Medical Department, Fee Validity, Lab Test, Observation, Service Request. Follow FHIR-style clinical terms (Observation, Diagnostic Report, Code Value).
- **Errors:** say what is wrong plus the fix ("Configure a service Item for {0}"). Prefix row errors as `Row #{0}: ...`. Use short titles ("Missing Configuration", "Not Allowed", "Mandatory", "Warning").
- **Confirmations** are questions ("Are you sure you want to mark this time as unavailable?"). Progress messages end with an ellipsis ("Creating unavailability record...").
- **i18n:** every string goes through `_()` or `__()` with `{0}` placeholders, not f-strings inside the translatable text. Translations come through Crowdin from `healthcare/locale/main.pot`.
- **Branding:** the product name is "Biograph". Marley branding was replaced by the `rebrand_marley_to_biograph` patch.
