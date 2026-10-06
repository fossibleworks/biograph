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
  - healthcare/public/js/healthcare_note.js
  - healthcare/locale/main.pot
  - crowdin.yml
  - healthcare/hooks.py
---

- **Terminology** follows clinical and FHIR naming used as DocType names in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Observation, Diagnostic Report, Service Request, Medication Request, Inpatient Record, Fee Validity, Insurance Payor. Reuse these exact terms and do not invent synonyms (write "Practitioner", not "Doctor").
- **Product name:** "Biograph" (the app title). Patch `rebrand_marley_to_biograph` replaced "Marley" in user-facing text.
- **Error tone:** short, direct sentences that name the record, usually ending with a period. Examples: "Appointment end must be after start.", "Patient {0} is not admitted in the service unit {1}", "Please set a Customer linked to the Patient". Titles are Title Case nouns: "Customer Not Found", "Practitioner Schedule Not Found", "Not Available". Some older strings use "Not allowed, ..." or an exclamation mark. Do not copy those.
- **Buttons and dialogs** use one verb in Title Case: "Add", "Create", "Done", "OK". Dialog titles take the form "Add Clinical Note" or "Create Service Request".
- Every string must be translatable (`_()` / `__()`), with numbered placeholders `{0}`, `{1}`. Avoid `{}` and JS template literals inside `__()`, because they break extraction into `main.pot`. Translations are managed through Crowdin.
