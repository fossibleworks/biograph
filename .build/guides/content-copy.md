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
  - healthcare/healthcare/doctype/insurance_claim/insurance_claim.py
  - healthcare/healthcare/doctype/patient_insurance_coverage/patient_insurance_coverage.py
  - patient_portal/src/PatientPortal.vue
  - healthcare/locale/main.pot
---

- **Always translatable:** use `_("...")` in Python and `__("...")` in JS. Use `{0}` placeholders with `.format()` rather than concatenation, for example `_("Clinical Procedure {0} already created from service request {1}")`. Strings feed `healthcare/locale/main.pot` and Crowdin.
- **Terminology** (use the DocType names exactly, in Title Case): Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Inpatient Record, Healthcare Service Unit, Medical Department, Lab Test, Sample Collection, Observation, Diagnostic Report, Service Request, Medication Request, Fee Validity, Insurance Payor, Insurance Claim. Use "Practitioner", not "Doctor", in UI copy.
- **Tone:** short, direct, clinical and administrative.
  - Buttons and actions use a verb or noun in Title Case: "Create", "Add", "Transfer", "Schedule Admission", "Book", "Pay Your Bill".
  - Statuses: "Active", "Completed", "Cancelled", "On Hold".
  - Validation messages are full sentences ending in a period, for example "Appointment end must be after start." Sometimes they use an exclamation mark ("Patient already has an appointment booked for the same day!"). Row errors cite the row ("Invalid Claim Amount, row #{}").
  - Dialog titles are short nouns, for example `title=_("Not Allowed")`.
  - Prompts use "Please select patient" / "Please review and cancel the invoice {0}".
- **Patient portal** (patient-facing, friendlier): "Book an Appointment", "Select a Department", "Select a Practitioner", "Payment Successful".
  - Empty states: "Looks like you don't have any appointments yet." and "No Records Found".
  - Labels end with colons in detail views ("Order Date:", "Collected On:").
- Units use the "Day(s)" / "Years(s)" pattern. Note that "Years(s)" is an existing typo.
