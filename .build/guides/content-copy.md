---
title: Content & Copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - patient_portal/src/components/Payment.vue
  - healthcare/locale/main.pot
  - healthcare/patches.txt
---

# Content and copy

- **Always translatable:** Python uses `_()` and JS uses `__()`, with positional `{0}` placeholders (`__("{0} Service Units created", [n])`). Strings flow into `healthcare/locale/main.pot` and from there to Crowdin.
- **Tone:** short, direct and in sentence case. Name the entity and the record: "Item {0} is not active", "No Inpatient Record found against patient {0}", "Start Date should be before End Date", "Configure a service Item for {0}". Dialog titles are short labels: "Not Allowed", "Missing Configuration", "No Drug Shortage".
- **Terminology:** use the DocType names exactly as they appear in the product, capitalised: Patient, Patient Appointment, Patient Encounter, Healthcare Practitioner, Healthcare Service Unit, Medical Department, Inpatient Record, Lab Test, Service Request, Medication Request, Fee Validity, Insurance Payor, Insurance Claim. Clinical concepts follow HL7 FHIR naming.
- **Portal copy** is patient-friendly: "Pay Your Bill", "Consultation Fee", "One-time registration for new patients". Note that portal Vue strings are currently not wrapped for translation.
- The brand name is **Biograph**. Do not reintroduce "Marley" in user-facing text.
