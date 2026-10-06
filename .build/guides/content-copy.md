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
  - crowdin.yml
---

- **Always translatable:** use `_()` in Python and `__()` in JS. Strings are extracted to `healthcare/locale/main.pot` and translated through Crowdin. Put variables in positional placeholders (`{0}`) applied with `.format()` *after* `_()`. Do not build the string with format first: `_("{0} is a holiday".format(date))` is a known anti-pattern.
- **Tone:** short and direct, in sentence or title case. It usually names the field or DocType: `Appointment Date and Time are required.`, `Registration Fee cannot be negative or zero`, `Configure a service Item for {0}`, `Patient already has an appointment booked for the same day!`.
- **Buttons and actions:** short Title Case verbs, such as `Reschedule`, `Check In`, `Make Payment`, `Mark Unavailable`, `Repeat Appointments`. Button groups get a group label like `Status`.
- **Dialog titles:** short nouns, such as `Missing Configuration` and `Not Available`.
- **Progress messages:** use an ellipsis, e.g. `Checking for conflicts...`.
- **Terminology:** use the DocType names exactly as written, capitalised: Patient Appointment, Healthcare Practitioner, Healthcare Service Unit, Medical Department, Patient Encounter, Fee Validity, Inpatient Record.
