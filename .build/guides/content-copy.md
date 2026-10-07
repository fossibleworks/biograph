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
  - healthcare/public/js/observation_widget.js
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Every user-facing string is translatable:** `_()` in Python, `__()` in Desk JS. The strings are harvested into `healthcare/locale/main.pot`, and Crowdin is configured (`crowdin.yml`). Do not build strings by concatenation inside the translation call. Use `{0}` placeholders and call `.format()` after `_()`.
- **Tone:** short, direct sentences in sentence case, usually ending with a period. Examples:
  - "Appointment Date and Time are required."
  - "Appointment end must be after start."
  - "Please select a Patient to be invoiced"
  - "SMS not sent, please check SMS Settings"
- Success alerts name the document: "Sales Invoice {0} created", "Customer {0} is created."
- **Terminology:** DocType names keep their capitals in copy (Patient, Healthcare Practitioner, Patient Appointment, Healthcare Settings, Service Unit, Medical Department). Use FHIR-aligned terms such as Service Request, Observation, and Medication Request.
- **Dialog titles and buttons** use Title Case verbs or nouns: "Add Observation", "Edit Observation", "Get Items From", "OK".
