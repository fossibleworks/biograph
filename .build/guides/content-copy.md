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
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/Payment.vue
  - healthcare/patches.txt
  - crowdin.yml
---

- **Terminology:** use the clinical/FHIR-aligned DocType names exactly as they appear in the UI. These include Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Observation, Diagnostic Report, Service Request, Medication Request, Inpatient Record, Fee Validity, Insurance Payor, and Therapy Plan. The product name is **Biograph** (rebranded from Marley via patch `rebrand_marley_to_biograph`).
- **Tone:** short, direct and instructional. Messages are sentence-case and usually end with a period, e.g. "Appointment end must be after start.", "Please set a Customer linked to the Patient", "Please select a Patient to be invoiced". Constraint violations often start with "Not allowed, …". "Please …" is the standard prompt form.
- **Titles and buttons** use Title Case: "Missing Configuration", "Customer Not Found", "Get Items From", "Add Observation", "Mark Time as Unavailable".
- **Placeholders:** use positional `{0}`, `{1}` with `.format()`. Bold document names in desk messages with `<b>{0}</b>` (e.g. "Patient <b>{0}</b> is not linked to a Customer"). Some legacy `{}` placeholders exist; prefer `{0}` in new code.
- **Patient-facing portal copy** is plainer and friendlier: "Pay Your Bill", "Consultation with {practitioner}", "One-time registration for new patients".
- **i18n:** every string goes through `_()` or `__()`. `main.pot` is regenerated weekly and translations come via Crowdin, so don't build sentences by concatenating fragments.
