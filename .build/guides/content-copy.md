---
title: Content & copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - patient_portal/src/PatientPortal.vue
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Translatable always:** `_()` in Python and `__()` in JS/Jinja. Strings are extracted into `healthcare/locale/main.pot` and translated through Crowdin.
- **Tone:** short, plain and clinical-administrative. Use Title Case for labels and actions ("Create", "Schedule Admission", "Reason for Cancellation", "Book an Appointment", "Select a Practitioner").
- **Domain terms:** use the DocType names exactly as written: Patient Appointment, Healthcare Practitioner, Medical Department, Healthcare Service Unit, Fee Validity, Inpatient Record, Service Request, Clinical Procedure, Lab Test, Observation, Code Value. Statuses: Active, Completed, Cancelled, On Hold.
- **Errors** state the problem directly, often naming the record with a `{0}` placeholder: "Invalid Code Value: {0}", "{0} is a holiday", "Appointment end must be after start.", "Not Allowed to cancel Nursing Task with status 'Completed'". Quote the status in single quotes. Use the title "Missing Configuration" for setup gaps, with an action such as "Configure a service Item for {0}".
- **Success messages:** "Sales Invoice {0} created", "Unavailability record cancelled successfully".
- **Portal empty states** are friendly: "Looks like you don't have any appointments yet.", "No Records Found".
- Units are pluralised with "(s)": "Day(s)", "Years(s)" (sic). Copy that pattern, but don't copy the typo.
