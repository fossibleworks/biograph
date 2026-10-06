---
title: Content and copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/public/js/observation_widget.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/utils.py
  - healthcare/locale/main.pot
---

- **Tone:** short, direct, clinical and administrative. Use Title Case for labels, headings and dialog titles: "Book an Appointment", "Available Slots", "Add Observation", "Mark Time as Unavailable", "Select a Practitioner".
- **Errors:** write a plain sentence that states the rule, usually ending with a period: "Appointment end must be after start.", "Registration Fee cannot be negative or zero", "Not Allowed to cancel Nursing Task with status 'Completed'". Quote document names and statuses in single quotes or with `frappe.bold`.
  - Error titles group the category: "Missing Configuration", "Not Available".
  - When something is missing, say what to configure: "Configure a service Item for {0}".
- **Empty states:** "No Records Found".
- **Terminology:** use the DocType names exactly as defined: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Observation, Diagnostic Report, Service Request, Fee Validity, Insurance Payor. Brand the app as **Biograph** (a patch renames Marley to Biograph).
- **i18n:** every string goes through `_()` or `__()` with `{0}` placeholders. Strings are extracted to `healthcare/locale/main.pot` and translated in Crowdin.
