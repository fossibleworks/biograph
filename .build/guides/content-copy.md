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
  - patient_portal/src/components/BookAppointmentModel.vue
  - patient_portal/src/PatientPortal.vue
  - healthcare/locale/main.pot
---

- **Terminology:** use the domain DocType names exactly and in Title Case: Patient, Patient Appointment, Patient Encounter, Healthcare Practitioner, Healthcare Service Unit, Medical Department, Lab Test, Sample Collection, Clinical Procedure, Inpatient Record, Insurance Payor, Healthcare Settings. Call the person "Practitioner", not "Doctor".
- **Error messages:** short, declarative sentences ending with a period, sometimes with an exclamation mark for conflicts (`"Appointment end must be after start."`, `"Appointment Date and Time are required."`, `"Patient already has an appointment booked for the same day!"`). Record names go in `{0}` placeholders, often wrapped in `frappe.bold`. Dialog titles are Title Case noun phrases (`Missing Configuration`, `Customer Not Found`).
- **Toasts:** past-tense confirmations (`"Sales Invoice {0} created"`).
- **Portal copy:** friendly and plain. Headings are Title Case (`Book an Appointment`, `Available Slots`, `Appointment Details`, `Pay Your Bill`, `Payment Successful`). Selectors use the "Select a …" form (`Select a Department`, `Select a Practitioner`). Empty states use "Looks like you don't have any appointments yet." or `No Records Found`. Button labels are short verbs (`Book`).
- All server strings use `_()` and all desk JS strings use `__()`, so they reach `healthcare/locale/main.pot` and Crowdin.
