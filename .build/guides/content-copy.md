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
  - healthcare/locale/main.pot
  - crowdin.yml
  - healthcare/hooks.py
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - healthcare/public/js/recurring_appointments.js
---

**Translation is mandatory.** All UI strings go through `_()` in Python and Jinja (about 277 uses) or `__()` in JS (about 824). They are extracted into `healthcare/locale/main.pot` and translated through Crowdin. Use `{0}`/`{1}` placeholders, never string concatenation, so translators can reorder:
- good: `_("No Inpatient Record found against patient {0}").format(patient)`
- avoid: building sentences like `__("Total conflicting appointments: ") + n`

**Tone:** short, direct and factual, in a clinical/administrative register. Errors state the problem, then the fix:
- "Patient already has an appointment booked for the same day!"
- "Appointment end must be after start."
- "Registration Fee cannot be negative or zero"
- "Configure a service Item for {0}"
- "Please set a valid Service Unit Capacity to enable Overlapping Appointments"
- "Please select patient"

Error dialog titles are short noun phrases: "Not Allowed", "Missing Required Fields", "Invalid Healthcare Service Unit", "Customer Not Found", "Validation Error".

**Buttons and labels** use Title Case verbs or nouns: "Create", "Add", "Edit", "Schedule Admission", "Schedule Discharge", "Transfer", "Change Item Code", "Reason for Cancellation", "Patient History".

**Terminology** (use the domain's DocType names exactly, in Title Case): Patient, Healthcare Practitioner (not "doctor"), Patient Appointment, Patient Encounter, Healthcare Service Unit / Service Unit Type, Medical Department, Inpatient Record, Lab Test, Observation, Diagnostic Report, Clinical Procedure, Service Request, Medication Request, Therapy Plan / Therapy Session, Fee Validity, Healthcare Settings. Statuses include "Open", "Scheduled", "Closed", "Cancelled", "Completed" and "Rejected". Reference records by name, using `get_link_to_form` where useful.

**Branding:** the product is **Biograph** (`app_title`). A v16 patch rebranded it from "Marley", so do not reintroduce "Marley Health" in UI copy.

Known legacy typos ("atleast", "Years(s)") exist. Do not copy them into new strings.
