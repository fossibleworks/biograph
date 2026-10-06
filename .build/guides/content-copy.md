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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - patient_portal/src/components/DiagnosticModel.vue
  - healthcare/locale/main.pot
  - crowdin.yml
  - healthcare/patches.txt
---

- **All user-facing strings are translatable:** `_()` in Python and `__()` in desk JS. They feed `healthcare/locale/main.pot`, which Crowdin manages (`crowdin.yml`). Use `{0}`/`{1}` placeholders with `.format()` and do not concatenate strings, so translators can reorder them.
- **Tone:** short, direct, clinical-admin language in sentence case, ending with a period. Examples:
  - "Appointment Date and Time are required."
  - "Appointment end must be after start."
  - "Please set a Customer linked to the Patient"
  - "Patient {0} is not admitted in the service unit {1}"
  - "Could not add conferencing to this Appointment, please contact System Manager"
- **Terminology:** capitalise DocType names when they mean the record type: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Healthcare Settings. Error dialog titles are short noun phrases, such as "Missing Configuration" and "Customer Not Found".
- **Buttons:** one or two words, Title Case verbs or nouns: "Save", "Cancel", "Reschedule", "View", "Patient History", "Create".
- **Portal empty states:** friendly and plain: "No Records Found", "Looks like you don’t have any orders yet.". Section labels are Title Case ("Appointment Details", "Test Report Details").
- The product name is **Biograph**. A patch rebranded Marley to Biograph (`rebrand_marley_to_biograph`), so do not add "Marley" to UI copy.
