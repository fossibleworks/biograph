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
  - healthcare/healthcare/doctype/healthcare_settings/healthcare_settings.js
  - healthcare/locale/main.pot
  - crowdin.yml
---

**Tone:** short, plain and direct. Copy is in English, with clinical and billing terms written in Title Case.

**Terminology:** use the DocType names as written, for example Patient Appointment, Healthcare Practitioner, Patient Encounter, Fee Validity, Healthcare Service Unit, Medical Department, Lab Test, Insurance Payor and Unavailability.

**Errors** (`frappe.throw`)
- Plain statements, usually with a trailing period, for example:
  - "Appointment Date and Time are required."
  - "Appointment end must be after start."
  - "Registration Fee cannot be negative or zero"
  - "Invalid Code Value: {0}"
  - "{0} is a holiday"
- Corrective hints are imperative: "Configure a service Item for {0}", "SMS not sent, please check SMS Settings".
- Configuration problems use the title "Missing Configuration".

**Confirmations** (`frappe.msgprint`): past tense, for example "Sales Invoice {0} created" and "Unavailability record cancelled successfully".

**Desk buttons and labels:** Title Case verb phrases, such as "Mark Unavailable" and "Link Customer to Patient".

**Patient Portal copy:** friendly Title Case headings and actions, such as "Book an Appointment", "Select a Department", "Select a Practitioner", "Pay Your Bill", "Payment Successful" and "Available Slots". The empty state is "No Records Found".

**Always translatable:**
- `_()` in Python and `__()` in desk JS, with `{0}` placeholders. Don't concatenate strings.
- Strings are extracted into `healthcare/locale/main.pot` and translated through Crowdin.
