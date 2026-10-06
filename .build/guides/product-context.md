---
title: Product context
category: product-context
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - README.md
  - pyproject.toml
---

**Biograph** (by Tacten / fossibleworks; the GitHub repo is `fossibleworks/biograph`, and Build calls it fossibleHIS) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians **Marley Health** with extra features. It ships as the Frappe app `healthcare` and adds the health domain to **ERPNext**. Much of the data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics and hospitals (clinical, front-desk, lab, nursing and billing staff use Frappe Desk), plus patients, who use the **Patient Portal** (`/patient-portal`).

**Main feature areas:**
- Patient management: patients, duplicate-patient checking, patient history and medical records
- Outpatient and inpatient care: Patient Appointment (including block-based and recurring booking), Patient Encounter, Inpatient Record, Fee Validity
- Clinical Procedures, Therapy/Rehabilitation/Physiotherapy, Nursing checklists
- Laboratory and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report
- Service Requests and Medication Requests (orders)
- Insurance: payors, contracts, policies, coverage, claims
- Medical code standards and FHIR terminology
- Regional: India ABDM integration (`healthcare/regional/india/abdm`)
- Billing is integrated with ERPNext Sales Invoice and Payment Entry.

ERPNext supplies the rest: pharmacy and stock, purchasing, HR, accounts and assets. Facilities are modelled as Healthcare Service Units, and specialities as Medical Departments.

**Branch context:** the fork's main branch is `biograph-fh`. It is being synced with upstream `earthians/marley` `version-16` (see `wiki/upstream-sync-version-16.md`). Fork behaviour wins over upstream when the two conflict.
