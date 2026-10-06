---
title: Content and copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/doctype/nursing_task/nursing_task.py
  - healthcare/locale/main.pot
  - healthcare/patches.txt
---

# Content and copy

- **All strings are translatable.** Use `_()` in Python and Jinja and `__()` in Desk JS. Strings are collected into `healthcare/locale/main.pot` and translated through Crowdin.
- **Domain terms.** Use the existing doctype labels exactly, in Title Case: *Patient*, *Healthcare Practitioner*, *Patient Appointment*, *Patient Encounter*, *Healthcare Service Unit*, *Medical Department*, *Inpatient Record*, *Lab Test*, *Clinical Procedure*, *Healthcare Settings*, *Fee Validity*, *Insurance Payor*. The product name is **Biograph**. The `rebrand_marley_to_biograph` patch shows that "Marley" should no longer appear in user-facing copy.
- **Error tone.** Errors are short, direct and imperative or declarative, and often name the record or field with a `{0}` placeholder and a link:
  - "Appointment end must be after start."
  - "Patient already has an appointment booked for the same day!"
  - "Please Configure Clinical Procedure Consumable Item in {0}" (title: "Missing Configuration")
  - "Not Allowed to cancel Nursing Task with status 'Completed'"
- **Desk buttons and actions** are short verbs or verb phrases: "Create", "Transfer", "Schedule Admission", "Schedule Discharge", "Process Transfer". Statuses are "Draft", "Active", "Completed", "Cancelled", "Rejected".
- **Patient Portal copy** is friendlier and in Title Case for headings and buttons: "Book an Appointment", "Select a Department", "Select a Practitioner", "Available Slots", "Pay Your Bill", "Payment Successful". Empty states read "No Records Found" followed by a plain sentence such as "Looks like you don't have any appointments yet."
- Keep placeholders as `{0}` with `.format()`. Do not concatenate translated fragments.
