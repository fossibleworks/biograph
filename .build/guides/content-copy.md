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
  - healthcare/public/js/service_request.js
  - patient_portal/src/components/Payment.vue
  - healthcare/www/patient-portal/index.py
  - crowdin.yml
---

- **Terminology** follows the clinical and FHIR domain and the DocType names: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Service Request, Medication Request, Healthcare Service Unit, Medical Department, Fee Validity, Inpatient Record. Use the exact DocType names in Title Case in messages. Older references to "Healthcare" stay as they are, because the app title is now "Biograph".
- **Error tone** is short, direct, and in sentence case, usually ending with a period: "Appointment Date and Time are required.", "Appointment end must be after start.", "Not permitted". A few use an exclamation mark ("Patient already has an appointment booked for the same day!"). Prefer the plain period form.
- **Buttons and labels** are short Title Case verbs or nouns: "Create", "Cancel", "Replace", "New Service Request", "Invoiced", "On Hold".
- **Empty states** use the pattern "No <Plural Entity>", e.g. "No Service Requests" or "No Medication Requests".
- **The patient-facing portal** uses friendlier second-person copy: "Pay Your Bill", "One-time registration for new patients".
- All strings go through `_()` or `__()` for translation, with Crowdin managing the locales. Avoid concatenating translated fragments; use format placeholders instead.
