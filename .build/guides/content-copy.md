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
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Tone:** short, plain and clinical-administrative. Labels are Title Case nouns ("Appointment Details", "Available Slots", "Consultation Fee", "Registration Fee", "Test Report Details"). Actions are verbs ("Book", "Create", "Refer Patient", "Schedule Admission", "Cancel Admission", "Schedule Discharge").
- **Empty states** are friendly and brief: "Looks like you don't have any appointments yet.", "No Records Found".
- **Errors** say what is wrong and, where possible, what to do: "Appointment end must be after start.", "Please select Patient", "Not allowed, cannot overlap appointment {}", "Could not add conferencing to this Appointment, please contact System Manager". Highlight record names and fields with `frappe.bold()`.
- **Terminology:** use the domain nouns as they appear in DocType names, in Title Case: Patient, Healthcare Practitioner ("Practitioner" in the portal), Patient Appointment, Patient Encounter, Inpatient Record, Healthcare Service Unit, Medical Department, Lab Test, Observation, Service Request, Medication Request, Insurance Payor, Fee Validity. The product is called **Biograph**.
- **Translation:** every string goes through `_()` (Python) or `__()` (JS) and is extracted to `healthcare/locale/main.pot` for Crowdin. Use positional placeholders (`{0}`), not concatenation.
