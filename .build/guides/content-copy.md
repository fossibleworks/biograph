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
  - healthcare/public/js/observation.js
  - healthcare/public/js/utils.js
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/src/components/BookAppointmentModel.vue
  - crowdin.yml
---

**Tone:** plain, direct and clinical-administrative. It is short, polite and has no jokes. Errors state the problem or rule ("Appointment end must be after start.", "Appointment Date and Time are required."). Some errors end with "!" for emphasis ("Patient already has an appointment booked for the same day!").

**Terminology** (match the DocType names, in Title Case): Patient, Healthcare Practitioner (shortened to "Practitioner" in the portal), Patient Appointment, Patient Encounter, Inpatient Record, Healthcare Service Unit, Medical Department, Lab Test, Sample Collection, Observation, Diagnostic Report, Clinical Procedure, Therapy Plan, Fee Validity, Insurance Payor, Healthcare Settings. Use "Appointment", "Encounter" and "Prescription" consistently.

**Patterns**
- Buttons and dialog titles are short verb phrases in Title Case: "Create", "Edit", "Add Observation", "Edit Observation", "Book an Appointment".
- Error dialog titles are short noun phrases: `title=_("Missing Configuration")`.
- Dynamic values use positional placeholders: `__("Mismatch in Code-data for row {0}", [row.idx])`, `_("... {0}").format(...)`. Never concatenate translated fragments.
- Portal empty states: a heading plus one friendly sentence ("No Records Found" / "Looks like you don't have any appointments yet.").
- Portal section labels are Title Case nouns: "Available Slots", "Appointment Details", "Test Report Details", "Payment Successful".

**Translation:** all desk strings go through `_()` / `__()`. They are extracted weekly to `healthcare/locale/main.pot` and translated in Crowdin. Note that portal Vue templates currently use hard-coded English.
