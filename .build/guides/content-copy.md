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
  - healthcare/healthcare/doctype/patient_encounter/patient_encounter.py
  - patient_portal/src/components/Payment.vue
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - crowdin.yml
  - healthcare/locale/main.pot
---

- **Tone:** short, plain, clinical-administrative sentences that end with a period, for example "Appointment Cancelled.", "Appointment end must be after start.", "Appointment Date and Time are required." and "Patient already has an appointment booked for the same day!". Exclamation marks are rare.
- **Titles and labels** use Title Case: "Missing Configuration", "Not Allowed", "Mandatory", "Mark Unavailable", "Therapy Session", "Entered In Error".
- **Interpolate record names** with `{0}` placeholders and bold them, for example `_("Therapy Plan {0} created successfully.").format(frappe.bold(doc.name))`. In JS use `__("{0} medication orders completed", [n])`.
- **Terminology:** follow the domain DocType names exactly: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Fee Validity, Lab Test, Observation, Therapy Plan, Insurance Payor. FHIR-style status values include "Entered In Error". The product name is **Biograph**; a v16 patch rebranded it from Marley.
- **Patient Portal copy** speaks to patients in friendly second person: "Pay Your Bill", "Details of fees", "Consultation with {{ practitioner }}", "One-time registration for new patients".
- **Translation:** every string must go through `_()` / `__()`. They are extracted into `healthcare/locale/main.pot` and translated via Crowdin (`crowdin.yml`). Portal Vue templates currently hard-code English.
