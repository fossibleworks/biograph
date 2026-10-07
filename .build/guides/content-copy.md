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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

**Tone:** direct, short and imperative, written for clinical and admin staff. Messages state what is wrong and usually how to fix it.

**Patterns observed**
- Validation: `"Appointment Date and Time are required."`, `"Appointment end must be after start."`, `"Registration Fee cannot be negative or zero"`, `"Code Value is required"`, `"Invalid Code Value: {0}"`.
- Configuration guidance: `"Please Configure Clinical Procedure Consumable Item in {0}"` (with a link to Healthcare Settings), `"Configure a service Item for {0}"`, title `"Missing Configuration"`.
- Not-allowed actions: `"Not Allowed to cancel Nursing Task with status 'Completed'"`.
- Availability: `"{0} is a holiday"` with the title `"Not Available"`, and `"No unavailability records found for the selected date."`
- Buttons are single verbs or short verb phrases in Title Case: `Reschedule`, `Confirm`, `Link Customer to Patient`.
- Background work: `"Appointments are being created in background"`.

**Terminology** (use the DocType names exactly, in Title Case): Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Clinical Procedure, Inpatient Record, Fee Validity, Healthcare Settings, Insurance Payor, Service Request, Observation, Diagnostic Report. The product name is **Biograph**. `rebrand_marley_to_biograph` renamed "Marley", so don't reintroduce it in copy.

**Mechanics**
- Every string is translatable: `_()` in Python and `__()` in JS. Use `{0}` placeholders with `.format()` and do not concatenate. Some legacy code calls `_("{0} is a holiday".format(date))`, which breaks translation; format *after* `_()`.
- Strings are extracted into `healthcare/locale/main.pot` and translated via Crowdin.
