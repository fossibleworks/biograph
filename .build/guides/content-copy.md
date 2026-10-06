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
  - healthcare/healthcare/utils.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Tone:** short, direct, clinical and operational. Validation messages are plain statements or imperatives, usually ending with a period. Examples:
  - "Appointment end must be after start."
  - "Registration Fee cannot be negative or zero"
  - "Configure a service Item for {0}"
  - "Patient already has an appointment booked for the same day!" (exclamation marks are rare)
- **Titles:** dialog titles are Title Case nouns, such as "Missing Configuration" and "Not Available".
- **Buttons:** short Title Case verbs or verb phrases, such as "Reschedule", "Confirm", "Check In" and "Make Payment". Buttons are grouped under menus such as "Status".
- **Terminology:** use the DocType names exactly, in Title Case (Patient Appointment, Patient Encounter, Healthcare Practitioner, Healthcare Service Unit, Medical Department, Fee Validity, Healthcare Settings). Field labels follow the doctype JSON labels.
- **Translation:** every string must be translatable with `_()` or `__()` and positional `{0}` placeholders. Strings flow into `healthcare/locale/main.pot` and on to Crowdin. Don't build sentences by concatenating translated fragments.
