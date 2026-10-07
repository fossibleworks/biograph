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
  - healthcare/locale/main.pot
  - crowdin.yml
---

**Tone:** short, plain and clinical-administrative. Messages state the problem directly and usually as a full sentence ending in a period. Exclamation marks show up only for warnings about blocked actions ("Patient already has an appointment booked for the same day!").

**Terminology:** use the domain DocType names in Title Case exactly as they are defined: *Patient*, *Healthcare Practitioner*, *Patient Appointment*, *Patient Encounter*, *Clinical Procedure*, *Nursing Task*, *Healthcare Service Unit*, *Medical Department*, *Fee Validity*, *Code Value*, *Insurance Payor*. Workflow status values are quoted in messages ("Not Allowed to 'Complete' Nursing Task without linking Task Document").

**Patterns:**
- Errors: `_("Appointment end must be after start.")`, `_("Invalid Code Value: {0}")`, `_("{0} is a holiday")`. Titles name the category, for example `"Missing Configuration"`.
- Buttons and actions: short Title Case verbs or verb phrases, such as `__("Book")`, `__("Check In")`, `__("Create Nursing Tasks")`, `__("Cancel Admission")`, `__("Confirm")`.
- Confirmations are phrased as questions ("Are you sure you want to book this time block appointment?"). Progress text uses an ellipsis ("Checking for conflicts...").
- Portal headings are Title Case ("Book an Appointment", "Available Slots", "Pay Your Bill", "Payment Successful"). The empty state is "No Records Found".

All copy must be translatable: `_()` in Python and `__()` in JS, with positional `{0}` placeholders. Translations flow through `healthcare/locale/main.pot` and Crowdin.
