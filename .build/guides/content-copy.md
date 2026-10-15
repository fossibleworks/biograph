---
title: Content and copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/public/js/observation.js
  - healthcare/public/js/mark_unavailable.js
  - patient_portal/src/components/DiagnosticModel.vue
  - healthcare/healthcare/doctype/insurance_payor_contract/insurance_payor_contract.py
  - healthcare/locale/main.pot
  - healthcare/patches.txt
---

- **Translation:** every user-facing string goes through `_()` (Python) or `__()` (JS) with `{0}`/`{1}` positional placeholders, e.g. `__("Permanently Submit {0}?", [this.docname])`. Strings are collected into `healthcare/locale/main.pot` and translated through Crowdin.
- **Tone:** short, factual, clinical and admin wording. No exclamation marks or chatty phrasing in product copy. Errors name the entity and the conflicting record, e.g. "An active contract for this Insurance Payor already exists: {0}", "Abbreviation is mandatory", "An Inpatient Medication Order {0} against Patient Encounter {1} already exists." Dialog titles group errors, e.g. `title=_("Missing Configuration")`. Light inline HTML such as `<b>Valid From</b>` is used to highlight field labels.
- **Terminology:** use DocType names exactly and in Title Case: Patient, Healthcare Practitioner (not "doctor"), Patient Appointment, Patient Encounter, Inpatient Record, Healthcare Service Unit, Medical Department, Lab Test, Clinical Procedure, Insurance Payor (spelled "Payor"), Service Request, Observation. Statuses follow FHIR-style wording such as Admitted.
- **Buttons and actions:** Title-Case verbs: "Create", "Add Observation", "Edit Observation", "Mark Time as Unavailable", "Book".
- **Empty states (portal):** a short Title-Case heading such as "No Records Found".
- Product name in UI is **Biograph**. The internal app and module name stays `healthcare`. A patch renamed Marley to Biograph, so don't reintroduce "Marley".
