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
  - healthcare/healthcare/doctype/lab_test/lab_test.js
  - healthcare/locale/main.pot
---

**Tone:** short, plain and instructional. Use sentence-style messages, often starting with "Please …" or "Not allowed, …". Examples:
- "Please select Patient"
- "Please set a Customer linked to the Patient"
- "Appointment end must be after start."
- "Not allowed, cannot overlap appointment {}"
- "Invalid Healthcare Service Unit"

**Terminology:**
- Use the domain nouns exactly as the DocType names, with capitals: Patient, Healthcare Practitioner, Patient Appointment, Healthcare Service Unit, Medical Department, Lab Test, Fee Validity.
- Refer to records by name, with placeholders such as "Patient {0} is not admitted in the service unit {1}".
- Bold dynamic values with `frappe.bold`.

**Portal copy:** Title Case labels and headings, for example "Book an Appointment", "Select a Department", "Select a Practitioner", "Available Slots", "Pay Your Bill", "Payment Successful", and the empty state "No Records Found".

**i18n:**
- Wrap every string in `_()` or `__()` so it reaches `main.pot` and Crowdin.
- Prefer numbered placeholders (`{0}`) over positional `{}` or f-strings.
