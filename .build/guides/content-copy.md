---
title: Content and copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/public/js/sales_invoice.js
  - healthcare/public/js/utils.js
  - healthcare/healthcare/utils.py
  - healthcare/permissions.py
  - crowdin.yml
  - healthcare/patches.txt
---

**Translation:** every user-facing string is wrapped in `_()` in Python or `__()` in JS (about 880 JS uses). Strings are extracted into `healthcare/locale/main.pot` and translated via Crowdin. Put variables in positional placeholders, e.g. `__("Error checking row {0}: {1}", [row.idx, e.message])`. Don't concatenate strings.

**Tone:** short, direct, imperative, often starting with "Please". Examples:
- "Please select Healthcare Service"
- "Please Configure Clinical Procedure Consumable Item in {0}" (the {0} links to the settings form)
- "You do not have permission to delete records."
- "No unavailability records found for the selected date."

**Titles and labels:**
- Dialog titles and labels use Title Case ("Missing Configuration", "Mark Unavailable", "Link Customer to Patient", "Show Payment Popup").
- Field descriptions are sentence case ("Checking this will popup to invoice appointment").

**Terminology:** follow the DocType names exactly:
- Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Healthcare Settings, Lab Test, Observation, Service Request, Insurance Payor.
- The product name is **Biograph**. Marley references were rebranded in patch `v16_0.rebrand_marley_to_biograph`.

Test data names are prefixed `_Test `.
