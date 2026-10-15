---
title: Content & Copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - patient_portal/src/components/BookAppointmentModel.vue
  - patient_portal/src/PatientPortal.vue
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/healthcare/doctype/clinical_procedure_template/clinical_procedure_template.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Terminology** follows the domain doctypes and FHIR/clinical vocabulary: Patient, Practitioner (Healthcare Practitioner), Medical Department, Healthcare Service Unit, Patient Appointment, Encounter, Inpatient Record, Lab Test, Observation, Service Request, Insurance Payor, Fee Validity. Use the DocType names exactly in messages.
- **Tone:** short, plain and Title Case for labels and headings ("Book an Appointment", "Select a Department", "Pay Your Bill", "Payment Successful", "Consultation Fee"). Errors are direct statements, e.g. "Item {0} is not active", "Not allowed to print this document.", "You do not have permission to delete records." Use a title such as "Missing Configuration" for configuration errors.
- **Empty states** in the portal are friendly and conversational, e.g. "Looks like you don't have any appointments yet." or "No Records Found".
- Field labels use a trailing colon in detail views ("Order Date:", "Collected On:").
- **i18n is mandatory.** Use `_()` in Python and `__()` in JS with `{0}` placeholders so strings are extracted into `healthcare/locale/main.pot` and translated through Crowdin. Do not build sentences by concatenating translated fragments.
