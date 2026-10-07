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
  - healthcare/locale/main.pot
---

- **Tone:** short, direct and clinical-administrative. Messages state what is wrong or required, e.g. "Appointment Date and Time are required.", "Appointment end must be after start.", "Healthcare Practitioner not available on {0}", "Configure a service Item for {0}". Some messages use imperative instructions ("Please select patient"), and some use "Not Allowed to ..." for permission or state errors.
- **Titles:** Title Case short phrases: "Missing Configuration", "Not Available", "Customer Not Found", "Invalid Healthcare Service Unit".
- **Buttons and actions:** single verbs or verb phrases in Title Case: "Create", "Transfer", "Schedule Admission", "Change Item Code", "Book".
- **Portal:** friendly Title Case headings: "Book an Appointment", "Select a Department", "Select a Practitioner", "Available Slots", "Pay Your Bill", "Payment Successful". The empty state is "No Records Found".
- **Terminology:** use the doctype names exactly: Patient, Healthcare Practitioner, Patient Appointment, Healthcare Service Unit, Medical Department, Inpatient Record, Service Request, Lab Test, Observation, Fee Validity, Insurance Payor. Units are written as "Day(s)" and "Years(s)".
- **i18n:** every string goes through `_()` or `__()` with `{0}` placeholders (no f-strings inside the translation call). Crowdin translates from `main.pot`.
