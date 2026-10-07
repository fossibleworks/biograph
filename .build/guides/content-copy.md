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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/Payment.vue
  - healthcare/patches.txt
  - crowdin.yml
---

- **Tone:** short, direct and clinical-administrative. Messages state the problem plainly and often name the fix, e.g. "Please Configure Clinical Procedure Consumable Item in {0}", "Appointment end must be after start.", "Patient already has an appointment booked for the same day!".
- **Terminology** follows the DocType names, in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Fee Validity, Insurance Payor, Healthcare Settings. Say "Practitioner", not "Doctor", in system copy.
- **Buttons** are short verbs or verb phrases in Title Case: "Reschedule", "Confirm", "Check In", "Make Payment", grouped under menus such as "Status".
- **Dialog titles:** use `title=_("Missing Configuration")` or `_("Not Available")`.
- **Portal copy** is friendlier and patient-facing: "Pay Your Bill", "Consultation Fee", "One-time registration for new patients".
- **i18n:** every string goes through `_()` or `__()` with `{0}` placeholders and `.format()`. Do not use f-strings or concatenation inside the translated string. Strings are extracted to `healthcare/locale/main.pot` and translated via Crowdin.
- **Brand:** "Biograph" (the `rebrand_marley_to_biograph` patch removed the old Marley naming from user-facing labels).
