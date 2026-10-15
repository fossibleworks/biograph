---
title: Content & Copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/healthcare_settings/healthcare_settings.py
  - healthcare/public/js/mark_unavailable.js
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/locale/main.pot
---

# Content and copy

- **Tone:** short, plain, declarative clinical and administrative language. Messages state the rule or the problem directly, for example "Appointment end must be after start.", "Registration Fee cannot be negative or zero", "Not allowed to print this document.", or "Patient already has an appointment booked for the same day!".
- **Casing:** labels and titles use Title Case ("Mark Time as Unavailable", "Healthcare Practitioner", "Reason for Unavailability", "Book an Appointment", "Available Slots"). Messages use sentence case.
- **Buttons** are short verbs: "Create", "Check Conflicts". Progress text ends with an ellipsis: "Checking for conflicts...".
- **Terminology:** use the DocType names exactly: Patient, Healthcare Practitioner, Patient Appointment, Healthcare Service Unit, Medical Department, Fee Validity, Inpatient Record, Lab Test, Observation, Service Request. The product name is **Biograph** (rebranded from Marley; see the `rebrand_marley_to_biograph` patch).
- **Interpolation:** use `{0}` placeholders with `frappe.bold()` around record names.
- **i18n:** every string goes through `_()` or `__()`. Strings are extracted to `healthcare/locale/main.pot` and translated through Crowdin. Some portal Vue copy is currently hardcoded English.
