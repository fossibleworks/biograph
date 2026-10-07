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
  - healthcare/public/js/observation.js
  - healthcare/public/js/sales_invoice.js
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/locale/main.pot
  - healthcare/patches.txt
---

- **Translation is mandatory:** wrap strings in `_()` in Python and `__()` in Desk JS. Strings are extracted to `healthcare/locale/main.pot` and translated through Crowdin. Do not build sentences by string concatenation; use `{0}` placeholders with `.format()`.
- **Tone:** short, direct and in sentence case, using clinical and ERP terms. Examples:
  - Errors: "Appointment end must be after start.", "Patient already has an appointment booked for the same day!", "Please select a Patient to be invoiced", "Configure a service Item for {0}", "Not Allowed to cancel Nursing Task with status 'Completed'".
  - Error titles: "Missing Configuration", "Not Available".
  - Actions and buttons: "Add Observation", "Edit Observation", "Get Items From", "Prescriptions"; portal: "Previous", "Next", "Book", "Pay".
  - Empty states: "No slots available".
- **Terminology:** write DocType names in Title Case as the domain nouns: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Clinical Procedure, Inpatient Record, Fee Validity, Insurance Payor, Service Request. The product name is **Biograph**; the `rebrand_marley_to_biograph` patch removed the "Marley" branding.
- Existing punctuation is mixed (some messages end with a period, some with "!"). For new copy, prefer one full sentence ending with a period.
- Portal Vue templates currently hard-code English labels, unlike Desk.
