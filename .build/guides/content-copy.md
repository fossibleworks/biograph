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
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

# Content & copy

## Tone
Copy is short, direct and clinical-operational. Errors name the record or field and the problem, with no blame and no jokes:
- "Appointment end must be after start."
- "No Inpatient Record found against patient {0}"
- "Configure a service Item for {0}"
- "Expected and Discharge dates cannot be less than Admission Schedule date"
- "Please select Patient to get Lab Tests"

An occasional exclamation mark appears on conflict errors ("Patient already has an appointment booked for the same day!"). Prefer a full stop in new copy.

## Terminology
- Use the DocType names verbatim and in Title Case when referring to records: *Patient*, *Healthcare Practitioner*, *Patient Appointment*, *Patient Encounter*, *Inpatient Record*, *Lab Test*, *Lab Test Template*, *Service Unit*, *Medical Department*, *Insurance Claim*, *Healthcare Settings*.
- Use *Practitioner*, not Doctor. Use *Encounter* for the consultation. Use *Admit* / *Admitted* / *Admission Scheduled* / *Discharge* for inpatient states.
- The product name is **Biograph** (the `rebrand_marley_to_biograph` patch removed "Marley").
- Buttons and actions use short Title Case verbs or nouns: "Admit", "Add Medication Orders", "Add Time Slots", "Actions".

## Mechanics
- Every string must be translatable. Use `_()` in Python and Jinja and `__()` in JS, with `{0}` positional placeholders. Never concatenate translated fragments. Strings flow into `locale/main.pot` and on to Crowdin.
- Success feedback uses `frappe.show_alert` (green indicator). Blocking problems use `frappe.msgprint` or `frappe.throw`.
