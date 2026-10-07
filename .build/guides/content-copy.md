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
  - patient_portal/src/components/DiagnosticModel.vue
  - healthcare/healthcare/utils.py
  - healthcare/locale/main.pot
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
---

- **Every string is translatable:** use `_()` in Python and `__()` in JS. Strings flow into `healthcare/locale/main.pot` and on to Crowdin, so build sentences with `{0}` placeholders instead of concatenating them.
- **Tone:** short, direct and declarative, often in Title Case for labels and actions: "Add Note", "Add Observation", "Check Conflicts", "Cancel Unavailability", "Book an Appointment", "Pay Your Bill".
- **Error messages** name the field or rule and end with a period where it reads as a sentence: "Appointment Date and Time are required.", "Appointment end must be after start.", "Invalid Code Value: {0}". Rule violations name the status in quotes: "Not Allowed to cancel Nursing Task with status 'Completed'". Configuration gaps say "Please Configure X in {link}" with the title "Missing Configuration".
- **Progress text** uses a present participle and an ellipsis: "Checking for conflicts...", "Creating unavailability record...".
- **Confirmations** are questions: "Are you sure you want to cancel this unavailability record?"
- **Empty states** in the portal: "No Records Found", "Looks like you don’t have any orders yet."
- **Terminology:** use DocType names as the canonical nouns (Patient, Healthcare Practitioner, Patient Appointment, Service Unit, Medical Department, Lab Test, Observation, Service Request, Fee Validity, Inpatient Record). The product name is "Biograph"; the v16 patch `rebrand_marley_to_biograph` replaced the earlier "Marley" branding.
