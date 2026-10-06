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
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/healthcare/utils.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Tone:** short, plain and directive, in sentence case or Title Case for actions. Errors name the problem and often the fix: "Appointment Date and Time are required.", "Appointment end must be after start.", "Please select a Patient to be invoiced", "Could not add conferencing to this Appointment, please contact System Manager".
- **Capitalise DocType names** as proper nouns in copy: Patient, Appointment, Practitioner, Healthcare Service Unit, Patient Encounter, Fee Validity, Sales Invoice.
- **Placeholders:** use `{0}`, `{1}` with `.format()` inside `_()` so translators can reorder them, e.g. `_("The practitioner {0} is already marked as unavailable during this time (see appointment {1})")`. Don't concatenate translated fragments.
- **Button and menu labels** are Title Case verbs or nouns: "Add Observation", "Edit Observation", "Get Items From", "Healthcare Services", "Prescriptions". Portal buttons are single words: "Previous", "Next", "Book", "Pay".
- **Error dialog titles** are short noun phrases such as "Missing Configuration".
- **Terminology:** "Practitioner" (not doctor), "Patient Encounter" (consultation), "Service Unit", "Medical Department", "Service Request", "Observation" (FHIR-aligned terms).
- **Translation:** every string goes through `_()` / `__()`. Strings are harvested into `healthcare/locale/main.pot` (Crowdin is configured via `crowdin.yml`). Note that the portal Vue templates currently hard-code English labels.
