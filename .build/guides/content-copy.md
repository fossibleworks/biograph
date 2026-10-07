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
  - healthcare/public/js/sales_invoice.js
  - patient_portal/src/components/Payment.vue
  - healthcare/locale/main.pot
  - crowdin.yml
---

**Tone:** plain, direct, clinical-admin vocabulary. Messages are short sentences in sentence case, usually ending with a period. Some use exclamation marks for blocking conflicts (`"Patient already has an appointment booked for the same day!"`).

**Patterns seen**
- Validation: state the requirement, e.g. `"Appointment Date and Time are required."`, `"Appointment end must be after start."`, `"Please select a Patient to be invoiced"`, `"Please select Healthcare Service"`.
- Soft failures and confirmations: `"Appointment Confirmation Message Not Sent"` (Title Case notice), `"Unavailability record cancelled successfully"`.
- Emphasize entity names in HTML: `"Patient <b>{0}</b> is not linked to a Customer"`.
- Portal copy is friendly and patient-facing: `"Pay Your Bill"`, `"Details of fees"`, `"Consultation with {practitioner}"`, `"One-time registration for new patients"`.

**Terminology:** use DocType names exactly and capitalize them as entities: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Service Request, Healthcare Settings. Use "Practitioner", not "Doctor", in generic copy.

**Translation is mandatory:** wrap every string in `_()` in Python and `__()` in JS, with `{0}` placeholders rather than concatenation, so it reaches `healthcare/locale/main.pot` and Crowdin. Portal strings are currently mostly hard-coded English in the Vue templates.
