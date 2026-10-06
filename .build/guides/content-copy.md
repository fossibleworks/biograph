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
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - healthcare/locale/main.pot
---

**Tone**
- Short, plain and clinical-administrative.
- DocType and field names appear in Title Case inside messages, exactly as they appear in the UI: "Healthcare Practitioner", "Fee Validity", "Receivable Account", "Nursing Task".

**Error messages**
- State the rule or what is missing, usually as a sentence without a trailing period. Examples:
  - "Appointment end must be after start."
  - "Start Date should be before End Date"
  - "Patient already has an appointment booked for the same day!"
  - "Configure a service Item for {0}"
  - "Not Allowed to cancel Nursing Task with status 'Completed'"
- Use `{0}` placeholders for record names. Quote status values in single quotes.

**Buttons and actions**
- One or two words in Title Case: "Book", "Check In", "Add Note", "Add Observation", "Cancel Unavailability", "Check Conflicts".
- Progress text ends with an ellipsis: "Checking for conflicts...", "Creating unavailability record...".
- Confirmations are questions: "Are you sure you want to mark this time as unavailable?"

**Portal (patient-facing)**
- Friendlier wording, with Title Case headings: "Book an Appointment", "Select a Department", "Available Slots", "Pay Your Bill", "Payment Successful".
- Empty states: "Looks like you don't have any appointments yet." and "No Records Found".

**Terminology**
- Use Patient, Healthcare Practitioner (Practitioner in short form), Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Inpatient Record, Lab Test, Observation, Diagnostic Report and Insurance Payor.
- Product name: "Biograph". Patch `rebrand_marley_to_biograph` renamed it from Marley.
- Spelling mixes British forms (authorise, organisations) with American ones.

**Translation**
- All strings go through `_()` / `__()` so they reach `main.pot` and Crowdin.
