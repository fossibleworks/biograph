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
  - healthcare/public/js/utils.js
  - healthcare/public/js/sales_invoice.js
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Translation:** every user-facing string must be translatable. Use `_()` in Python and `__()` in JS, with positional placeholders (`_("Invalid Code Value: {0}").format(v)`, `__("Error checking row {0}: {1}", [row.idx, e.message])`).
- **Tone:** short, direct and clinical. Messages state the problem or requirement plainly:
  - "Code Value is required"
  - "Appointment end must be after start."
  - "{0} is a holiday"
  - "Registration Fee cannot be negative or zero"
  - "Patient already has an appointment booked for the same day!"
  
  Actionable hints use an imperative: "Configure a service Item for {0}", "Please select Healthcare Service". Dialog titles are Title Case nouns, such as "Missing Configuration" and "Appointment Conflicts Detected".
- **Labels and buttons:** Title Case verb phrases, such as "Add Time Slots", "Add Medication Orders" and "Add Exercise Step". Statuses are Title Case ("Admission Scheduled", "Admitted", "Open", "Scheduled", "Closed").
- **Terminology:** use the DocType names as written:
  - Patient
  - Healthcare Practitioner (not "doctor")
  - Patient Appointment
  - Patient Encounter
  - Healthcare Service Unit
  - Medical Department
  - Inpatient Record
  - Lab Test
  - Fee Validity
  - Insurance Payor (spelled "Payor")
  - Healthcare Settings
  
  The product name is "Biograph".
- **Translation files:** strings are extracted into `healthcare/locale/main.pot` and translated through Crowdin.
