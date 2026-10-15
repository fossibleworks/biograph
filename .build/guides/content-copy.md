---
title: Content & Copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient/patient.js
  - healthcare/healthcare/doctype/clinical_procedure/clinical_procedure.py
  - healthcare/healthcare/doctype/clinical_procedure_template/clinical_procedure_template.py
  - healthcare/healthcare/doctype/lab_test/lab_test_list.js
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

## Tone

Copy is short, plain and clinical-operational. Validation messages use Title Case nouns for DocType and field names, and are often polite imperatives:

- "Please save the patient first"
- "Please select a Patient Encounter to get from"
- "Only numbers are allowed in the Mobile No field."
- "Price List is mandatory" (title: "Price List Not Set")
- "Item {0} is not active" / "Item with Item Code {0} already exists"
- "Not allowed to print this document."
- Error dialog titles: "Insufficient Stock", "Appointment Confirmation Message Not Sent".

Buttons and labels are one or two words in Title Case: "Create", "Cancel", "Status", "Completed", "Clinical Note", "Reason for Cancellation", "Change Item Code". Unit labels use the form "Day(s)" and "Years(s)". Empty-result messages read like "No Lab Tests created".

## Terminology

Refer to records by their exact DocType names in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Service Request, Inpatient Record, Fee Validity, Insurance Payor. The product name is **Biograph**; Marley branding was replaced by the `rebrand_marley_to_biograph` patch, so do not reintroduce "Marley".

## Translation

Every string must be translatable: `_()` in Python, `__()` in JS, with `{0}` placeholders. Strings are pulled into `healthcare/locale/main.pot` and translated through Crowdin. Do not wrap field keys or internal identifiers in `_()`. Some existing code does this (e.g. `_("encounter")` in patient_portal.py), and it should not be copied.
