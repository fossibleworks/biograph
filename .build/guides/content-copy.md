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
  - healthcare/healthcare/utils.py
  - healthcare/public/js/sales_invoice.js
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/patches.txt
  - healthcare/locale/main.pot
---

- **Tone:** plain, direct, clinical-operational. Messages are short sentences in sentence case. Imperatives start with "Please …" ("Please set a Customer linked to the Patient", "Please select a Patient to be invoiced", "Please Configure Clinical Procedure Consumable Item in {0}").
- **Refusals** follow "Not allowed, …" ("Not allowed, cannot overlap appointment {}"). Conflicts state the fact ("Patient already has an appointment booked for the same day!"). Dialog titles are short nouns ("Missing Configuration", "Customer Not Found").
- **Terminology:** use the DocType names exactly and in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Clinical Procedure, Inpatient Record, Fee Validity, Healthcare Settings, Insurance Payor. The product name is **Biograph** (rebranded from Marley, see patch `rebrand_marley_to_biograph`).
- **Portal copy:** short Title Case labels and headings ("Book an Appointment", "Select a Department", "Available Slots", "Consultation Fee", "Pay Your Bill", "Payment Successful"). Empty states are friendly ("Looks like you don't have any appointments yet.", "No Records Found").
- **i18n:** every string goes through `_()` / `__()` with positional `{0}` placeholders so `main.pot` can extract it. Don't build sentences by concatenation.
