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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment_list.js
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Translatable always:** wrap Python strings in `_()` and JS strings in `__()`. Strings are extracted to `healthcare/locale/main.pot` and synced via Crowdin.
- **Tone:** short, direct, sentence case, clinical and administrative.
  - Validation messages state the rule, e.g. "Appointment end must be after start." or "Patient already has an appointment booked for the same day!".
  - Interpolate entity names with `{0}` and `frappe.bold()`, e.g. "The practitioner {0} is already marked as unavailable during this time (see appointment {1})".
- **Success toasts:** "Sales Invoice {0} created", "Unavailability record cancelled successfully".
- **Warnings** say what failed and where to fix it: "SMS not sent, please check SMS Settings".
- **Buttons:** Title Case verbs: "Reschedule", "Check In", "Make Payment", "Mark Unavailable", "Repeat Appointments". Group them under menus such as "Status".
- **Error titles:** Title Case, e.g. "Missing Configuration", "Appointment Confirmation Message Not Sent".
- **Terminology:** use the doctype names exactly: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Inpatient Record, Fee Validity, Healthcare Settings.
