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
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/patches.txt
  - healthcare/locale/main.pot
  - crowdin.yml
---

# Content and copy

## Tone
- Error messages are short, direct and in sentence case, and usually end with a period. Some older strings end with `!`.
  - "Appointment Date and Time are required."
  - "Appointment end must be after start."
  - "Patient already has an appointment booked for the same day!"
  - "Registration Fee cannot be negative or zero"
- Errors that block an action use the pattern "Not Allowed to …" ("Not Allowed to cancel Nursing Task with status 'Completed'").
- Configuration problems tell the user what to set up ("Configure a service Item for {0}") and use the title "Missing Configuration".
- In messages, DocType names keep **Title Case** (Patient Appointment, Healthcare Practitioner, Nursing Task, Fee Validity). Use the exact DocType labels.

## Portal copy
- Headings and labels are Title Case: "Book an Appointment", "Select a Department", "Select a Practitioner", "Available Slots", "Pay Your Bill", "Payment Successful", "Test Report Details".
- Empty state: "No Records Found".

## Terminology
- Use **Practitioner** (not doctor), **Patient Encounter** (not visit), **Healthcare Service Unit**, **Medical Department**, **Inpatient Record**, **Fee Validity**, **Therapy Session**, **Lab Test**, **Observation**, **Service Request**.
- The brand is **Biograph**. Marley was rebranded (patch `rebrand_marley_to_biograph`). Do not add new "Marley" strings.

## i18n
- Wrap every string in `_()` (Python) or `__()` (JS). Put placeholders as `{0}` inside the translated string and call `.format()` outside it. Avoid `_("..".format(x))`; legacy code still does this.
- Translations flow through `healthcare/locale/main.pot` and Crowdin.
