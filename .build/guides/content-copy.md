---
title: Content and copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - patient_portal/src/components/Payment.vue
  - healthcare/locale/main.pot
  - README.md
---

- **Translation:** every string goes through `_()` in Python and `__()` in JS so that it reaches `locale/main.pot` and Crowdin. Use `{0}` placeholders with `.format()` and never concatenate translated fragments.
- **Tone:** short, direct, domain-specific sentences in Title Case for DocType and field names: "Registration Fee cannot be negative or zero", "Start Date should be before End Date", "Price List is mandatory", "No Inpatient Record found against patient {0}", "Configure a service Item for {0}".
- **Prompts:** "Please select …" ("Please select patient", "Please select a Medication").
- **Confirmations:** past tense, with a link to the record: "Sales Invoice {0} created", "Customer {0} updated".
- **Buttons and actions:** single verbs or verb + noun: "Create", "Add", "Transfer", "Schedule Admission", "Change Item Code". Dialog titles: "Not Allowed", "Missing Configuration".
- **Terminology:** Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Inpatient Record, Healthcare Service Unit, Medical Department, Fee Validity, Service Request, Observation, Diagnostic Report, Code Value. Use the DocType names exactly. Spelling is British ("organisations").
- **Portal copy:** friendly and second-person: "Pay Your Bill", "One-time registration for new patients".
