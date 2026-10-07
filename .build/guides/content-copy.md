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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/public/js/sales_invoice.js
  - healthcare/patches.txt
  - crowdin.yml
---

- **Tone:** short, direct and instructional, in sentence case. Examples: "Please select Healthcare Service", "Appointment end must be after start.", "Please Configure Clinical Procedure Consumable Item in {0}". Dialog titles are Title Case nouns, such as "Missing Configuration".
- **Terminology:** use the DocType names exactly as nouns: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Clinical Procedure, Inpatient Record, Fee Validity, Healthcare Settings. The product name is **Biograph**. Older "Marley" branding was rebranded by the `v16_0.rebrand_marley_to_biograph` patch, so do not reintroduce it.
- **i18n:** every string goes through `_()` / `__()` with positional `{0}` placeholders. Do not concatenate strings, because they are extracted to `healthcare/locale/main.pot` and translated through Crowdin.
- Link to the relevant settings form (`get_link_to_form`) when a message asks the user to configure something.
