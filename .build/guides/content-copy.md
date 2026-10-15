---
title: Content and copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/clinical_procedure/clinical_procedure.py
  - healthcare/healthcare/doctype/clinical_procedure_template/clinical_procedure_template.js
  - healthcare/healthcare/doctype/healthcare_settings/healthcare_settings.py
  - healthcare/patches/v16_0/rebrand_marley_to_biograph.py
  - healthcare/locale/main.pot
  - crowdin.yml
---

- **Translation is mandatory.** Wrap every user-facing string: Python `_()`, Desk JS `__()`. Strings flow into `healthcare/locale/main.pot`, then to Crowdin, then to `.po` files. Use positional placeholders (`{0}`, `{1}`) so translators can reorder them.
- **Tone:** short, plain and direct, in sentence-like Title Case for labels and action buttons:
  - Buttons: `Change Item Code`, `Sync`, `Print`, `Book`, `OK`.
  - Freeze messages end with an ellipsis: `Syncing Documents ...`.
- **Error messages** state the problem and name the record:
  - `Item {0} is not active`
  - `User {0} is already assigned to Healthcare Practitioner {1}`
  - `Registration Fee cannot be negative or zero`
- **Instruction errors** start with "Please": `Please set Customer in Patient {0}`, `Please enable pop-ups`.
- **Dialog titles** are short noun phrases in Title Case: `Customer Not Found`, `Price List Not Set`, `Already Exist`, `Google Calendar Required`.
- **Status labels** are Title Case words (`Pending`, `In Process`, `Completed`, `Open`, `Scheduled`) and must match the DocType Select options exactly.
- **Terminology:** use the DocType names verbatim: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Service Request, Clinical Procedure, Lab Test, Therapy Session, Inpatient Record. The product name in UI is **Biograph** (a v16 patch rebrands from Marley). Use British/Indian spelling as in the README ("organisations").
- Highlight record names with `frappe.bold()` in messages.
