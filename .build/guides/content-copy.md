---
title: Content & copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - .github/workflows/generate-pot-file.yml
---

- **Tone:** plain, direct and clinical-administrative. Short Title Case labels for buttons and section headers ("Create", "Schedule Admission", "Book an Appointment", "Available Slots", "Test Report Details").
- **Validation messages:** one sentence stating the rule, in sentence case with a full stop, naming the doctype or field. Examples: "Appointment end must be after start.", "Registration Fee cannot be negative or zero", "{0} is a holiday", "Not Allowed to 'Complete' Nursing Task without linking Task Document". Use `{0}` placeholders, never f-strings, inside `_()`.
- **Empty states (portal):** a heading and a friendly line, e.g. "No Records Found" + "Looks like you don't have any appointments yet."
- **Terminology:** use the doctype names exactly as written: Patient, Healthcare Practitioner, Patient Appointment, Service Unit, Medical Department, Inpatient Record, Lab Test, Observation, Diagnostic Report, Fee Validity, Insurance Payor. The product is called **Biograph** (Marley branding was removed by the `rebrand_marley_to_biograph` patch).
- Every string is translatable: `_()` in Python and `__()` in JS. These strings feed the weekly POT regeneration.
