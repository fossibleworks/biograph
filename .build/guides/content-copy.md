---
title: Content & Copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/healthcare_settings/healthcare_settings.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/inpatient_record/inpatient_record.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/locale/main.pot
---

# Content and copy

- **Translatable always:** Python `_("...")`, desk JS `__("...")`. Use `{0}` placeholders instead of string concatenation, so translators see whole sentences (`_("No Inpatient Record found against patient {0}")`). Strings flow into `healthcare/locale/main.pot` and are translated through Crowdin.
- **Tone:** short, direct, imperative, plain clinical/admin vocabulary, no exclamation marks.
  - Errors state the problem: `"Registration Fee cannot be negative or zero"`, `"Item {0} is not active"`, `"Price List is mandatory"`.
  - Instructions start with *Please*: `"Please select Patient to get prescribed procedure"`, `"Please enable pop-ups"`.
  - Configuration problems use the title `"Missing Configuration"`.
- **Labels and buttons:** Title Case nouns or verb phrases, e.g. `"Add Observation"`, `"Add Medication Orders"`, `"Admission Scheduled"`, `"Appointment Duration (mins)"`.
- **Terminology:** use the DocType names exactly: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Inpatient Record, Healthcare Service Unit, Medical Department, Lab Test, Observation, Service Request, Insurance Payor, Fee Validity. Write "Practitioner", not "Doctor". Product name: **Biograph** (the v16 patch rebrands Marley).
- **Patient portal** copy is friendlier and second-person: `"Book an Appointment"`, `"Payment Successful"`, `"Your appointment with {name} has been confirmed."`, placeholder `"Choose a patient"`.
