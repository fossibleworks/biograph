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
  - healthcare/healthcare/doctype/nursing_task/nursing_task.py
  - healthcare/healthcare/utils.py
  - healthcare/locale/main.pot
---

**Tone:** short, plain and clinical-administrative.

**Terminology:** use the DocType names exactly and in Title Case:
- Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter
- Healthcare Service Unit, Medical Department, Fee Validity
- Nursing Task, Inpatient Record, Sales Invoice, Healthcare Settings

**Errors** are short declarative sentences, sometimes with a fix hint:
- "Appointment end must be after start."
- "Patient already has an appointment booked for the same day!"
- "Configure a service Item for {0}"
- "Not Allowed to cancel Nursing Task with status 'Completed'"

Dynamic values go in `{0}` placeholders, often as form links. Status values in errors are wrapped in single quotes.

**Confirmations** state what happened: "Sales Invoice {0} created", "Customer {0} is created.", "Unavailability record cancelled successfully".

**Empty states** state the condition: "No pending medication orders found for selected criteria".

**Buttons and labels** are short Title Case verbs or nouns: "Create", "Add", "Transfer", "Change Item Code", "Reason for Cancellation", "From Date" / "To Date".

**Translation:** every string must be wrapped in `_()` or `__()`, because `healthcare/locale/main.pot` is regenerated from them. Do not build sentences by joining translated fragments; use placeholders.
