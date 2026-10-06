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
  - healthcare/public/js/mark_unavailable.js
  - patient_portal/src/components/Payment.vue
  - healthcare/healthcare/doctype/patient/patient.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Tone:** plain, concise, clinical-administrative. Write short imperative or declarative sentences.
  - Errors: "Appointment Date and Time are required.", "Appointment end must be after start.", "Patient not found", "Not allowed to print this document."
  - Confirmations: "Are you sure you want to cancel this unavailability record?"
  - Progress: "Checking for conflicts...", "Creating unavailability record..."
- **Capitalisation:** buttons and labels use Title Case ("Check In", "Add Observation", "Cancel Unavailability", "Check Conflicts"). Dialog titles are Title Case ("Appointment Conflicts Detected", "Duplicate Patient"). Messages are sentence case with a final period. A few legacy messages end in `!`.
- **Terminology:** use domain DocType names exactly: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Clinical Procedure, Lab Test, Observation, Service Request, Insurance Payor. Interpolate record names with `{0}` and `frappe.bold`.
- **Patient-facing portal copy** is friendlier and simpler: "Pay Your Bill", "Consultation Fee", "One-time registration for new patients", "Book".
- **Translation:** all strings go through `_()` / `__()`. They are extracted weekly into `healthcare/locale/main.pot`, with Crowdin configured in `crowdin.yml`. Don't concatenate translated fragments. Use placeholders instead.
