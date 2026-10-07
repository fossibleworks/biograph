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
  - healthcare/locale/main.pot
---

**Tone:** short, plain and clinical-administrative. Labels use Title Case, and messages are full sentences ending with a period.

- **Buttons and actions** are short verbs or Title Case phrases: "Create", "Transfer", "Schedule Admission", "Change Item Code", "Book an Appointment", "Pay Your Bill".
- **Status words** come from the domain: "Open", "Scheduled", "Completed", "Active", "Not Active".
- **Errors** state the rule and name the record with `frappe.bold`: "Appointment end must be after start.", "Patient already has an appointment booked for the same day!", "Not allowed, {0} cannot exceed maximum capacity {1}". Dialog titles are short, for example "Missing Configuration" and "Not Allowed".
- **Prompts:** "Please select patient".
- **Portal empty states** are friendly and second person: "No Records Found" / "Looks like you don’t have any orders yet."
- **Terminology:** use the domain DocType names exactly (Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Practitioner Availability, Fee Validity, Service Request, Observation). The product name is "Biograph", and the module is "Healthcare".
- **Translation:** all copy goes through `_()` / `__()` and ends up in `healthcare/locale/main.pot` (Crowdin). Use positional `{0}` placeholders, not concatenation.
