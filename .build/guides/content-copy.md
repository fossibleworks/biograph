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
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/locale/main.pot
  - healthcare/patches.txt
---

- **Tone:** short, plain and direct. Messages often start with "Please ..." for required actions ("Please set a Customer linked to the Patient", "Please enter {}"). Use "Not allowed, ..." for blocked actions. Exclamation marks appear only rarely ("Patient already has an appointment booked for the same day!").
- **Terminology:** use domain DocType names in Title Case inside copy: Patient, Healthcare Practitioner, Patient Appointment, Healthcare Service Unit, Inpatient Record, Fee Validity, Healthcare Settings. In UI text, "practitioner" is the word for a clinician. When pointing users to an administrator, say "System Manager".
- **Formatting:** interpolate with `{0}`/`{1}` placeholders inside `_()` and wrap entity names in `frappe.bold()`. Error titles are short Title Case nouns ("Missing Configuration", "Invalid Healthcare Service Unit").
- **Translation:** every string must be translatable (`_()` in Python, `__()` in JS) because strings are extracted to `healthcare/locale/main.pot` and translated through Crowdin.
- **Portal empty states:** "No Records Found" and "No slots available". Errors appear as toasts.
- **Branding:** the product is "Biograph". Patch `rebrand_marley_to_biograph` replaced "Marley" in user-facing strings, so do not reintroduce "Marley" in UI copy.
