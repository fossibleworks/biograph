---
title: Content and copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/public/js/healthcare_note.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/patient_encounter/patient_encounter.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Tone:** short, plain and imperative. Use Title Case for button and dialog labels, such as `Add Clinical Note`, `Create Service Request`, `Reschedule`, `Cancel Unavailability`, `Patient History`. Primary actions are single verbs: `Add`, `Create`, `Done`, `Save`, `View`, `Book`.
- **Messages** are sentence case and end with a period when they are full sentences: `"Appointment Date and Time are required."`, `"Appointment end must be after start."`, `"Patient history has been updated."`. Short status messages may drop the period: `"Patient not found"`, `"Customer {0} created and linked to Patient"`.
- **Row validation** uses the format `"Row #{0} (Drug Prescription): Drug Code is mandatory"`.
- **Terminology:** use the DocType names exactly and capitalised, since they are the domain vocabulary: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Service Request, Observation, Lab Test, Therapy Session, Insurance Payor / Policy / Coverage / Claim, Healthcare Settings. When pointing to a setting, bold its name: `<b>Automate Appointment Invoicing</b>`.
- **Translation:** every string goes through `_()` or `__()` with positional `{0}` placeholders so it can be extracted into `healthcare/locale/main.pot` and translated through Crowdin. Do not build sentences by concatenating translated pieces.
