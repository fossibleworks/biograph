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
  - healthcare/public/js/healthcare_note.js
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/src/components/DiagnosticModel.vue
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

**Tone:** short, plain and clinical-administrative. Messages are sentence-style statements, and many end with a period or an exclamation mark, for example `"Patient already has an appointment booked for the same day!"`, `"Appointment end must be after start."` and `"Appointment Date and Time are required."`.

**Titles and buttons** are Title Case and short: `"Add Clinical Note"`, `"Create Service Request"`, `"Invalid Healthcare Service Unit"`, `"Customer Not Found"`. Primary actions are single verbs: `"Add"`, `"Create"`, `"Done"`.

**Terminology:** use the DocType names exactly as they appear in the UI: Patient, Patient Appointment, Patient Encounter, Healthcare Practitioner, Healthcare Service Unit, Medical Department, Observation, Diagnostic Report, Service Request, Medication Request, Fee Validity, Therapy Plan, Insurance Payor. The product name is **Biograph**. Patch `v16_0/rebrand_marley_to_biograph` replaced the earlier "Marley" branding, so do not reintroduce "Marley" in user-facing text.

**Statuses** use Title Case words: Open, Scheduled, Confirmed, Checked In, Checked Out, Closed, Cancelled; and for diagnostics Collected, In Progress, Completed, Approved, Not Approved, Rejected, Partly Paid. Use the British spelling **Cancelled**.

**Portal copy** is friendly but brief: `"Failed to load appointments"`, `"Please enable pop-ups"`, and section labels such as `"Afternoon"`.

**i18n:** every string goes through `_()` in Python or `__()` in desk JS. Interpolate with `{0}` placeholders, never with f-strings inside `_()`. Strings feed `healthcare/locale/main.pot`, which is translated through Crowdin.
