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
  - healthcare/public/js/mark_unavailable.js
  - healthcare/public/js/observation.js
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/src/components/BookAppointmentModel.vue
  - crowdin.yml
---

# Content and copy

- **Always translatable:** use `_()` in Python and `__()` in desk JS. Strings are extracted to `healthcare/locale/main.pot` and translated through Crowdin.
- **Use healthcare domain terms consistently:** Patient, Healthcare Practitioner (shortened to "practitioner" in prose), Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Observation, Fee Validity, Inpatient Record, Insurance Payor and Healthcare Settings. Refer to doctypes by their title-case names.
- **Error tone:** plain and direct. State the problem and, where possible, name the conflicting record in bold:
  - "Appointment Date and Time are required."
  - "Appointment end must be after start."
  - "Patient already has an appointment booked for the same day!"
  - "The practitioner {0} is not available during this time due to an unavailability record {1}"
  - Config errors use the title "Missing Configuration".
- **Buttons and dialog titles:** short verb phrases in title case: "Create", "Add Observation", "Edit Observation", "Mark Time as Unavailable", "Book an Appointment".
- **Field labels:** title case: "Healthcare Practitioner", "From Time", "Unavailability For".
- **Empty states (portal):** short headings such as "No Records Found" and "No slots available".
- **Statuses** are capitalised doctype status values: Open, Scheduled, Confirmed, Closed, Cancelled.
- Some portal copy is currently hard-coded English in Vue templates. New portal strings should still be easy to translate.
