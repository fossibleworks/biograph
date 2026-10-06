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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - healthcare/healthcare/doctype/nursing_task/nursing_task.py
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/locale/main.pot
---

# Content and copy

- **Translatable everywhere:** Python uses `_("...")` and JS uses `__("...")`. Strings are collected into `healthcare/locale/main.pot` and translated in Crowdin, so don't concatenate translated fragments. Use positional `{0}` placeholders with `.format()`.
- **Tone:** short, direct, and imperative or declarative. Messages are often a single sentence, with or without a trailing period. Examples:
  - "Appointment Date and Time are required."
  - "Appointment end must be after start."
  - "Patient already has an appointment booked for the same day!"
  - "Registration Fee cannot be negative or zero"
  - "Configure a service Item for {0}"
  - "Not permitted"
  - "Customer {0} is created." (alert)
- **Terminology:** use the DocType names in Title Case exactly as defined: Patient Appointment, Patient Encounter, Healthcare Practitioner, Healthcare Service Unit, Lab Test, Clinical Procedure, Therapy Session, Inpatient Record, Nursing Task, Service Request, Medication Request, Insurance Payor. Quote status values in single quotes, e.g. `'Completed'`.
- **Buttons:** short verbs or nouns, grouped under `View` or `Create` (Reschedule, Cancel, Patient History, Clinical Procedure).
- **Portal empty states:** plain title-case phrases such as "No Records Found" and "No slots available".
