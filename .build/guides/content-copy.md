---
title: Content & Copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - public/js/mark_unavailable.js
  - healthcare/public/js/healthcare_note.js
  - healthcare/healthcare/doctype/clinical_procedure_template/clinical_procedure_template.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - crowdin.yml
---

# Content and copy

- **Always translatable**: `_()` in Python and `__()` in desk JS. Strings are extracted to `healthcare/locale/main.pot` and translated through Crowdin.
- **Tone**: short, direct and clinical-administrative. Title Case for labels, dialog titles and actions ("Mark Time as Unavailable", "Reason for Unavailability", "Check Conflicts", "New Clinical Note"). Sentence case for messages and confirmations ("Are you sure you want to mark this time as unavailable?", "From Time must be before To Time").
- **Errors** name the record and the problem, with placeholders: "Item {0} is not active", "Item with Item Code {0} already exists", "Not allowed to print this document.". Add a short title for modal errors ("Insufficient Stock", "Not Allowed", "Cannot mark as unavailable!").
- **Empty states**: "No Clinical Notes", "No slots available".
- **Progress**: "Checking for conflicts...".
- **Terminology**: use the DocType names exactly as defined: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Inpatient Record, Lab Test, Clinical Procedure, Therapy Session, Insurance Payor. Use FHIR-aligned terms (Service Request, Observation, Diagnostic Report, Code System, Value Set).
- The product name is **Biograph**. The v16 patch `rebrand_marley_to_biograph` removed "Marley" branding, so do not reintroduce it.
