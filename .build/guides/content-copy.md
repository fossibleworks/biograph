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
  - healthcare/public/js/sales_invoice.js
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/patches.txt
  - healthcare/locale/main.pot
---

- **Tone:** direct, plain sentences, and mostly polite imperative ("Please select Healthcare Service", "Please enter {}").
- **Validation messages** state the conflict and name the record. For example:
  - "The practitioner {0} is not available during this time due to an unavailability record {1}"
  - "Not allowed, cannot overlap appointment {}"
  - "Patient already has an appointment booked for the same day!"
- **Field names in messages** are bolded with `frappe.bold`.
- **Terminology:** Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Observation, Diagnostic Report, Therapy Session, Insurance Payor. Use the doctype names exactly.
- **Product name:** the product is "Biograph" (a v16 patch rebranded it from Marley). Do not introduce "Marley" in user-facing copy.
- **Translation:** all copy is translatable (`_()` / `__()`) and harvested into `healthcare/locale/main.pot`.
- **Dialog titles** use Title Case, e.g. "Book an Appointment" and "Missing Configuration".
