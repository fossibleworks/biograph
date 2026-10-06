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
  - healthcare/public/js/sales_invoice.js
  - healthcare/public/js/utils.js
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/PractitionerSelector.vue
  - healthcare/patches.txt
  - healthcare/locale/main.pot
---

- **Tone:** short, direct, clinical and administrative. Validation messages are usually one sentence with a full stop or exclamation mark, for example "Appointment end must be after start.", "Appointment Date and Time are required." and "Patient already has an appointment booked for the same day!".
- **Instructions:** start with "Please …", for example "Please select Healthcare Service" and "Please select Drug".
- **Error dialog titles:** use Title Case nouns, such as "Missing Configuration".
- **Terminology:** use the domain DocType names exactly and in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Observation, Fee Validity, Inpatient Record, Healthcare Settings. The brand is **Biograph**; the `rebrand_marley_to_biograph` patch removed "Marley" from user-facing strings.
- **Placeholders:** use `{0}` (`_("… {0}").format(x)` / `__("… {0}", [x])`), for example "Mismatch in Code-data for row {0}".
- **Portal copy:** headings use sentence or title case ("Select a Practitioner"), plus short status text ("Page {{ page }} of {{ totalPages }}").
- **Translation:** every string goes through `_()`/`__()`. `main.pot` is regenerated weekly and Crowdin syncs the translations.
