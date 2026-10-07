---
title: Content and copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/public/js/sales_invoice.js
  - healthcare/healthcare/utils.py
  - healthcare/locale/main.pot
---

- **Tone:** direct, instructional and polite, usually starting with "Please ...": "Please select a Patient to be invoiced", "Please Configure Clinical Procedure Consumable Item in {0}", "Please select Healthcare Service".
- **Error titles** are short Title Case noun phrases: "Missing Configuration", "Customer Not Found", "Invalid Healthcare Service Unit". Messages name the setting and link to it (`get_link_to_form`). Use `<b>` around record names (`Patient <b>{0}</b> is not linked to a Customer`).
- **Terminology:** use domain doctype names in Title Case exactly as defined: Patient, Healthcare Practitioner, Patient Appointment, Healthcare Service Unit, Medical Department, Healthcare Settings, Fee Validity, Inpatient Record, Lab Test, Observation, Service Request, Clinical Procedure. Billing terms follow ERPNext (Sales Invoice, Customer, Item). Abbreviations in use: "OP Consulting Charge", "Inpatient Visit Charge".
- **Buttons and menus:** short verbs and groups, e.g. "Add", "Get Items From" → "Prescriptions", "Healthcare Services".
- **Translation:** every string goes through `_()` or `__()` with positional `{0}` placeholders. Don't build sentences by concatenating fragments, because translators see `main.pot` entries only.
