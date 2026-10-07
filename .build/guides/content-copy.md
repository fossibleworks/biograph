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
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_encounter/patient_encounter.js
  - healthcare/locale/main.pot
  - crowdin.yml
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
---

- **Every string is translatable:** `_()` in Python/Jinja and `__()` in JS. Strings are extracted to `healthcare/locale/main.pot` and translated via Crowdin.
- **Placeholders:** use `{0}`, `{1}` with `.format()` *outside* `_()`, e.g. `_("Patient {0} is not admitted in the service unit {1}").format(...)`. Older code uses `{}`; prefer the numbered form for new strings.
- **Tone:** short, direct, sentence case, written for clinical and admin staff.
  - Instructions start with "Please …": "Please set a Customer linked to the Patient", "Please enter {}".
  - Prohibitions use "Not allowed, …": "Not allowed, cannot overlap appointment {}".
  - Confirmations state facts: "Sales Invoice {0} created", "{0} has fee validity till {1}".
- **Error titles** are short noun phrases in Title Case: "Missing Configuration", "Customer Not Found", "Invalid Healthcare Service Unit".
- **Terminology:**
  - Use DocType names exactly as they appear in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Inpatient Record, Fee Validity, Sales Invoice.
  - Say "Practitioner", not "doctor", in system copy.
  - The product brand is "Biograph". "Marley" was rebranded via a v16 patch.
