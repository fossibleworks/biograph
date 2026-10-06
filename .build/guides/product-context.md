---
title: Product Context
category: product-context
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - README.md
  - healthcare/hooks.py
  - pyproject.toml
  - healthcare/www/patient-portal/index.py
  - healthcare/regional/india/abdm/utils.py
---

**Biograph** (by Tacten / FossibleWorks, tracked internally as *fossibleHIS*) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with extra features on top. It ships as the Frappe app `healthcare` and adds the healthcare domain to **ERPNext**. Much of its data model follows **HL7 FHIR**.

**Who uses it:** healthcare practitioners, clinics and hospitals. That means clinical staff (doctors, nurses, lab and therapy staff), front-desk and billing users working in Frappe Desk, and patients using the web Patient Portal.

**Main feature areas** (from the README and the doctype names under `healthcare/healthcare/doctype/`):
- Patient management: registration, duplicate-check rules, medical records, patient history and progress pages
- Outpatient care: Patient Appointment, Patient Encounter, Fee Validity, Practitioner Schedule and Availability
- Inpatient care: Inpatient Record, Inpatient Medication Order and Entry, Discharge Summary, Nursing Tasks
- Clinical procedures, rehabilitation and physiotherapy: Therapy Plan, Therapy Session, Exercise Types
- Laboratory and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report, Specimen
- Medications and Service Requests (orders)
- Insurance: Payor, Contract, Eligibility Plan, Claim, Coverage
- Medical code standards: Code System and Code Value
- India regional ABDM integration under `healthcare/regional/india/abdm`

The app relies on ERPNext for pharmacy and stock, purchasing, HR, accounts, and invoicing (Sales Invoice and Payment Entry hooks). Facilities are modelled as **Healthcare Service Units** and specialities as **Medical Departments**.

**Entry points:** the Desk home is `/desk/healthcare` (`app_home` in `hooks.py`). Patients use the Vue patient portal at `/patient-portal`, plus web forms for appointments, registration, lab tests and prescriptions.

**Fork context:** this repo's default branch is `biograph-fh`. There is ongoing work to bring in upstream earthians/marley `version-16` commits, tracked in `wiki/upstream-sync-version-16.md`.
