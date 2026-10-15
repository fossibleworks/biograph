---
title: Content & Copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/public/js/healthcare_note.js
  - healthcare/public/js/patient_quick_entry.js
  - healthcare/public/js/mark_unavailable.js
  - patient_portal/src/PatientPortal.vue
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/controllers/service_request_controller.py
  - healthcare/locale/main.pot
  - healthcare/patches.txt
---

## Tone

The copy is plain, clinical and administrative. It is short and direct, and it uses healthcare domain terms as nouns.

## Terminology

Use the DocType names exactly as written, in Title Case: *Patient*, *Healthcare Practitioner* ("Practitioner" in the portal), *Patient Appointment*, *Patient Encounter*, *Medical Department*, *Healthcare Service Unit*, *Lab Test*, *Observation*, *Service Request*, *Medication Request*, *Fee Validity*, *Inpatient Record*. The product name is **Biograph**. The `v16_0.rebrand_marley_to_biograph` patch renamed it from "Marley", so do not reintroduce "Marley Health" in UI copy.

## Patterns

- **Buttons and labels** are Title Case verb + noun: "Add Clinical Note", "Create Medication Request", "Create Service Request", "Book an Appointment", "Pay Your Bill", "Invite as User".
- **Field labels** are Title Case nouns: "First Name", "Mobile Number", "Blood Group", "Birth Date".
- **Errors** are sentences that say what is wrong: "Appointment end must be after start.", "From Time must be before To Time", "Only numbers are allowed in the Mobile No field." Dialog titles are short nouns such as "Missing Configuration" and "Not Allowed".
- **Empty states** in the portal are friendly: "Looks like you don't have any appointments yet." and "No Records Found". Use a straight apostrophe. One string uses a curly ’, so keep new strings consistent with the straight form.
- **Loading states** use the form "Loading Slots...".
- **Success** messages are short: "Payment Successful".

## Translation

Every string must be translatable: `_()` in Python and Jinja, `__()` in Desk JS. Strings are extracted to `healthcare/locale/main.pot` and translated through Crowdin, so avoid building sentences by concatenation. Prefer `_("... {0}").format(x)` over f-strings inside `_()`, because the translation catalog cannot extract the interpolated forms. Some existing code (`service_request_controller.py`) uses `_(f"...")`. Do not copy that pattern.
