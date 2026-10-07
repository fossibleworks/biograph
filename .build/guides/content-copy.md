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
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/utils.py
  - healthcare/locale/main.pot
---

- **Tone:** short, direct, and declarative. Copy often ends with a period, and occasionally uses `!` for conflicts ("Patient already has an appointment booked for the same day!").
- **Terminology:** use Title Case domain/DocType nouns exactly as defined: Patient, Healthcare Practitioner, Patient Appointment, Inpatient Record, Healthcare Service Unit, Medical Department, Lab Test, Observation, Clinical Procedure, Therapy Session, Insurance Payor, Fee Validity. The product name is **Biograph**; Marley branding was replaced (see the `rebrand_marley_to_biograph` patch).
- **Patterns:**
  - Field-constraint errors: "Appointment end must be after start.", "Expected and Discharge dates cannot be less than Admission Schedule date".
  - Row errors are prefixed `Row #{0}:`.
  - Missing setup errors use the title "Missing Configuration".
  - Action buttons are concise verbs: Reschedule, Confirm, Check In, Make Payment, grouped under menus like "Status".
- **i18n:** every string goes through `_()` / `__()` with positional `{0}` placeholders, so translators get `healthcare/locale/main.pot`. Don't build sentences by concatenating translated fragments.
