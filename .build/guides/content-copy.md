---
title: Content & copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/patches.txt
  - crowdin.yml
---

**Tone:** plain, direct, clinical and administrative. Use short imperative or declarative sentences that end with a period for validation messages: "Appointment Date and Time are required.", "Appointment end must be after start.", "Please select Healthcare Service", "No unavailability records found for the selected date."

**Patterns**
- Errors name the field or record and the problem: `"Invalid Code Value: {0}"`, `"Code Value is required"`. Grouped errors get a Title Case title ("Missing Configuration").
- Blocking explanations lead with a bold summary followed by the remedy: "**Cannot book time block appointment!** The following appointments conflict…" then "**Important:** You must cancel these appointments before…"
- Buttons are short Title Case verbs: Reschedule, Confirm, Check In, Make Payment. In the portal they are single words: Previous, Next, Book, Pay, Close, OK. Progress messages read "Checking for conflicts..."
- Dialog titles: "Book an Appointment".

**Terminology** (use the DocType names exactly): Patient, Healthcare Practitioner ("Practitioner" in short UI), Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Observation, Diagnostic Report, Service Request, Medication Request, Inpatient Record, Fee Validity, Insurance Payor, and Practitioner Availability (formerly "Time Block"). The product name is **Biograph**, so don't write "Marley" (a patch rebranded it).

**i18n:** wrap every string in `_()` or `__()` so it lands in `locale/main.pot` for Crowdin. Put placeholders in `{0}` and don't concatenate translated fragments. The portal Vue templates currently hard-code English.
