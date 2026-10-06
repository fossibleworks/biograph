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
  - healthcare/healthcare/doctype/healthcare_settings/healthcare_settings.py
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/Payment.vue
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - healthcare/locale/main.pot
---

- **Terminology** comes from the healthcare domain, as DocType names: *Patient*, *Healthcare Practitioner* (not "doctor"), *Patient Appointment*, *Patient Encounter*, *Healthcare Service Unit*, *Medical Department*, *Fee Validity*, *Service Request*, *Observation*, *Inpatient Record*, *Therapy Plan*, *Insurance Payor*. The product is "Biograph". The app and module name is "Healthcare".
- **Error tone** is short, direct sentences in sentence case, often naming the conflicting record: "Appointment end must be after start.", "Patient already has an appointment booked for the same day!", "The practitioner {0} is not available during this time due to an unavailability record {1}", "Registration Fee cannot be negative or zero", "Configure a service Item for {0}". Configuration problems use the dialog title "Missing Configuration". Prefer this direct style over legacy informal strings like "Oops!..".
- **Error log titles** describe what failed: "Appointment Confirmation Message Not Sent", "Unavailability Calendar Event Error".
- **Portal copy** is friendly and plain for patients: headings like "Pay Your Bill", labels "Consultation Fee", "Registration Fee", helper text "One-time registration for new patients".
- **Translation:** every user-facing string goes through `_()` or `__()`, with `{0}` positional placeholders. Translations flow through `locale/main.pot` and Crowdin.
