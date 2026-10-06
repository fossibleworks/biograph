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
  - healthcare/healthcare/doctype/patient/patient.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Tone:** short, plain, clinical-administrative. Sentence case for messages, Title Case for buttons, labels, and headings ("Add Observation", "Mark Time as Unavailable", "Book an Appointment", "Pay Your Bill").
- **Errors** state the problem directly and end with a period or exclamation mark: "Appointment end must be after start.", "Patient already has an appointment booked for the same day!", "From Time must be before To Time". Use the dialog `title=` for a short category ("Not Available", "Customer Not Found").
- **Progress and confirm text:** "Checking for conflicts...", "Are you sure you want to mark this time as unavailable?"
- **Success toasts** name the document: "Sales Invoice {0} created", "Customer {0} created and linked to Patient".
- **Empty states:** "No Records Found".
- **Terminology:** Patient, Healthcare Practitioner, Healthcare Service Unit, Medical Department, Appointment, Fee Validity, Service Request, Observation, Lab Test, Inpatient Record. Use the DocType names as written.
- **i18n:** every string goes through `_()` (Python) or `__()` (JS), with `{0}` positional placeholders filled by `.format()`. Strings are extracted into `healthcare/locale/main.pot` and translated via Crowdin.
