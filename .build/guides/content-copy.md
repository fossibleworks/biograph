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
  - healthcare/public/js/sales_invoice.js
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/AppointmentModel.vue
  - healthcare/locale/main.pot
---

- **Tone:** plain, direct and clinical-administrative. Messages are mostly short sentences in sentence case, often ending with a period or `!`. Examples:
  - "Appointment Date and Time are required."
  - "Patient already has an appointment booked for the same day!"
  - "Please set a Customer linked to the Patient"
- **Pattern for blocked actions:** "Not allowed, …" (e.g. "Not allowed, cannot overlap appointment {}").
- **Ask for missing configuration with "Please …"**, e.g. "Please select Healthcare Service". Use the title "Missing Configuration".
- **Terminology:** use DocType names, capitalised as nouns: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Code Value, Fee Validity, Inpatient Record, Healthcare Settings. Use "practitioner", not "doctor", in system copy.
- **Placeholders:** `{0}`/`{1}`, with record names emphasised via `frappe.bold()`. Always translatable via `_()` / `__()`. Strings feed `healthcare/locale/main.pot`.
- **Portal empty states:** a friendly heading plus an explanation, e.g. "No Records Found" / "Looks like you don't have any appointments yet."
