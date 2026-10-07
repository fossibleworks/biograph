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
  - healthcare/public/js/observation_widget.js
  - patient_portal/src/components/Payment.vue
  - healthcare/patches.txt
  - healthcare/locale/main.pot
---

**Tone**: plain, direct and clinical-administrative. Messages are short sentences in sentence case with a final period or `!`.
- "Appointment end must be after start."
- "Patient already has an appointment booked for the same day!"
- "Please select a Patient to be invoiced"

**Conventions**
- Refer to records by their DocType name in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Healthcare Service Unit, Lab Test, Sales Invoice. Bold the specific record with `frappe.bold()` or `<b>{0}</b>`.
- Instructions use "Please select …" or "Please set …".
- Configuration errors use the dialog title "Missing Configuration".
- Button and action labels are Title Case verbs: "Get Items From", "Add Observation", "Edit Observation", "Create", "New Service Request".
- Empty states are short noun phrases, for example "No Observations".
- Portal copy speaks to the patient in the second person: "Pay Your Bill", "Consultation with {{ practitioner }}", "One-time registration for new patients".
- Domain terms follow FHIR and HIS vocabulary: Encounter, Observation, Service Request, Diagnostic Report, Practitioner, Service Unit, Fee Validity, Inpatient Record.
- The product name is **Biograph**. Older "Marley" branding was replaced by the `rebrand_marley_to_biograph` patch.
- All strings must be translatable (`_()` / `__()`). They flow into `healthcare/locale/main.pot` for Crowdin.
