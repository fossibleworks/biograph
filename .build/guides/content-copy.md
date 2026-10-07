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
  - healthcare/healthcare/utils.py
  - healthcare/public/js/mark_unavailable.js
  - healthcare/locale/main.pot
  - crowdin.yml
  - patient_portal/src/components/AppointmentModel.vue
---

- **All copy is translatable:** wrap it in `_()` in Python and `__()` in JS/Jinja. Strings are harvested into `healthcare/locale/main.pot` and translated via Crowdin (`crowdin.yml`).
- **Tone:** short, direct and factual. Use sentence-style messages that name the DocType and field in Title Case.
  - Validation: "Appointment end must be after start.", "Appointment Date and Time are required.", "Registration Fee cannot be negative or zero", "Configure a service Item for {0}".
  - Not-allowed: "Not Allowed to cancel Nursing Task with status 'Completed'".
  - Confirmation: "Are you sure you want to mark this time as unavailable?"
  - Progress: "Creating unavailability record..."
  - Dialog titles: "Missing Configuration".
- **Placeholders:** use positional `{0}` with `.format()`. Never use f-strings inside `_()`.
- **Terminology:** use the domain DocType names consistently: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Inpatient Record, Lab Test, Observation, Diagnostic Report, Fee Validity, Insurance Payor. The product name is **Biograph** (rebranded from Marley via the `rebrand_marley_to_biograph` patch).
- **Buttons:** short verbs, e.g. "Create", "Cancel", "Book", "Add Observation", "Get Items From". Statuses are Title Case ("On Hold", "Invoiced", "Active").
