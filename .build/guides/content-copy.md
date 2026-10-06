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
  - healthcare/healthcare/doctype/nursing_task/nursing_task.py
  - healthcare/public/js/mark_unavailable.js
  - crowdin.yml
  - .github/workflows/generate-pot-file.yml
  - README.md
---

# Content and copy

- **Every** user-facing string must be translatable: `_()` in Python and `__()` in JS. Crowdin handles the translations, and a weekly job regenerates the POT file.
- **Tone**: short, direct, sentence-style messages that state the rule or problem. For example:
  - "Appointment Date and Time are required."
  - "Appointment end must be after start."
  - "Registration Fee cannot be negative or zero"
  - "Configure a service Item for {0}"
  - "Not Allowed to cancel Nursing Task with status 'Completed'"
  - Exclamation marks appear occasionally ("Patient already has an appointment booked for the same day!"). Prefer a neutral tone in new copy.
- **Terminology**: use the DocType names exactly as labels, in Title Case: *Patient*, *Healthcare Practitioner*, *Healthcare Service Unit*, *Medical Department*, *Patient Encounter*, *Patient Appointment*, *Fee Validity*, *Inpatient Record*, *Lab Test*, *Insurance Payor*, *Healthcare Settings*. Say "Practitioner" (not "Doctor") and "Service Unit" (not "Room" or "Ward").
- Dialog titles and field labels are Title Case ("Mark Time as Unavailable", "From Time").
- Pass dynamic values as `{0}` placeholders, formatted outside the translation call.
- Spelling mixes British and Indian English in places ("organisations" in the README). Keep existing labels unchanged so translations do not break.
