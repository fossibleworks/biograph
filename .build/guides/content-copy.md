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
  - healthcare/public/js/healthcare_orders.html
  - healthcare/public/js/healthcare_note.html
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/public/js/sales_invoice.js
  - healthcare/patches.txt
  - crowdin.yml
---

- **Always translatable**: Python `_()`, JS `__()`, Jinja `{{ __("...") }}`. Strings feed `healthcare/locale/main.pot` and Crowdin. Use positional placeholders `{0}`, `{1}` inside the string. Do not concatenate translated fragments.
- **Terminology** uses the DocType names in Title Case: *Patient*, *Healthcare Practitioner*, *Patient Appointment*, *Patient Encounter*, *Healthcare Service Unit*, *Medical Department*, *Fee Validity*, *Lab Test*, *Clinical Procedure*, *Inpatient Record*, *Service Request*, *Insurance Payor*. Use "Practitioner", not "Doctor", in UI.
- **Error/validation tone**: short, direct, sentence case, often ending with a period or `!`. Examples: "Patient already has an appointment booked for the same day!", "Appointment end must be after start.", "Not allowed, cannot overlap appointment {}", "Invalid Healthcare Service Unit", "Please enter {}". Bold field names with `<b>…</b>` where helpful.
- **Empty states** follow the pattern "No <Things>" or "No Records Found" ("No Service Requests", "No Clinical Notes").
- **Buttons and headings** are Title Case and imperative: "Book an Appointment", "Pay Your Bill", "Select a Department", "Select a Practitioner", "Get Items from Prescriptions", "Add".
- Brand: the product is **Biograph**. Patch `rebrand_marley_to_biograph` replaced the earlier "Marley" branding, so do not reintroduce "Marley" in user-facing copy.
