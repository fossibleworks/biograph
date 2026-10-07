---
title: Content & copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/utils.py
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/locale/main.pot
  - crowdin.yml
---

**Tone:** plain, short and operational, written for clinical and front-desk staff. Copy is in sentence case or Title Case and has no exclamation marks in product UI.

**Patterns in use**
- **Confirmations:** `"Sales Invoice {0} created"`, `"Customer {0} is created."`, `"Patient history has been updated."`, `"Unavailability record cancelled successfully"`.
- **Errors:** state what failed, then point to the fix. Examples: `"SMS not sent, please check SMS Settings"`, `"Could not load patient history: {0}"`, `"Error updating patient history: {0}"`, and dialogs titled `"Missing Configuration"`.
- **Guidance and imperatives:** `"Please select a Patient to be invoiced"`, `"You must cancel these appointments before marking this time as unavailable."`
- **Confirmation prompts:** `"Are you sure you want to mark this time as unavailable?"`
- **Progress text:** `"Creating unavailability record..."`
- **Buttons and actions:** short verbs, such as `Create`, `Add`, `Cancel`, `Replace`, `Add Observation`, `Get Items From`, and `Book` in the portal.
- **Empty states:** `"No pending medication orders found for selected criteria"`.
- **Statuses:** Title Case words such as `Open`, `Scheduled`, `Closed`, `On Hold`, `Active` and `Invoiced`.

**Terminology:** use the DocType names exactly as they appear, in Title Case: Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Medical Department, Lab Test, Clinical Procedure, Inpatient Record, Fee Validity, Healthcare Settings, Observation, Service Request. The product name is "Biograph" and the module is "Healthcare".

**Translation**
- Every string goes through `_()` in Python or `__()` in JS.
- Insert values with `{0}` placeholders, not concatenation, so translators can reorder them.
- Strings are extracted into `healthcare/locale/main.pot` and translated through Crowdin.
