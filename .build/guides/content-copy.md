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
  - patient_portal/src/components/Payment.vue
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - crowdin.yml
  - healthcare/locale/main.pot
---

- **Terminology:** use clinical and HIS terms that match the DocType names: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Fee Validity, Inpatient Record, Insurance Payor, Service Request. The product is **Biograph** (the `rebrand_marley_to_biograph` patch shows it was renamed from Marley). Keep "Healthcare" as the module/workspace name.
- **Error messages** are short, sentence case, and name the documents involved:
  - "Patient already has an appointment booked for the same day!"
  - "Not allowed, cannot overlap appointment {}"
  - "Please set a Customer linked to the Patient"
  - Use Title Case dialog titles: "Customer Not Found", "Not Available", "Practitioner Schedule Not Found".
- **Success notices** report what happened: "Sales Invoice {0} created", "Appointment Cancelled."
- **Patient portal copy** is friendly and direct with simple headings: "Pay Your Bill", "Consultation Fee", "One-time registration for new patients", button "Book".
- **i18n:** all backend strings go through `_()`, Desk JS through `__()`, with `{0}` placeholders so Crowdin can translate them (`healthcare/locale/main.pot`). Portal Vue copy is currently hard-coded English.
