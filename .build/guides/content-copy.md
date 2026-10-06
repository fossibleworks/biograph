---
title: Content & Copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/public/js/sales_invoice.js
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/Payment.vue
  - healthcare/locale/main.pot
  - crowdin.yml
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
---

- **Translatable strings everywhere:** use `_()` in Python and Jinja, and `__()` in JS, with positional `{0}` placeholders (`__("Patient <b>{0}</b> is not linked to a Customer", [name])`). Strings are extracted to `healthcare/locale/main.pot` and translated through Crowdin. Never concatenate translated fragments.
- **Tone:** short, direct and instructional, in Title Case for labels and buttons, sentence case for messages. Messages start with "Please" when asking the user to act:
  - "Please select a Patient to be invoiced"
  - "Please select Healthcare Service"
  - "Please select Drug"
- **Error titles** are short Title Case nouns: "Missing Configuration", "Appointment Confirmation Message Not Sent".
- **Buttons and dialogs:** use verb phrases such as "Get Items From", "Add", "Get Items from Healthcare Services" and "Permanently Submit {0}?".
- **Terminology:** use the DocType names exactly, capitalised as entities: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Lab Test, Service Request, Insurance Payor (spelled *Payor*), Therapy Plan. Wrap record names in `<b>` in messages.
- **Patient portal copy** is friendlier and addressed to the patient ("Pay Your Bill", "Details of fees", "Consultation with {practitioner}", "One-time registration for new patients").
- **Brand:** the product is "Biograph". The `rebrand_marley_to_biograph` patch shows that user-visible text should say Biograph, not Marley.
