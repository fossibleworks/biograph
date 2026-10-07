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
  - healthcare/www/patient_portal.py
---

**Biograph (fossibleHIS) by Tacten/FossibleWorks** is an open-source Hospital Information System (HIS). It is a fork of earthians' Marley Health with extra features. It ships as the Frappe app `healthcare` and adds the health domain to ERPNext.

**Users:** healthcare practitioners, clinics, hospitals, and their patients, through the patient portal.

**Feature areas:**
- Patient management
- Outpatient and inpatient management
- Patient appointments, including block-based therapy booking and recurring appointments
- Clinical procedures
- Rehabilitation and physiotherapy (therapy plans and sessions)
- Laboratory and diagnostics (lab tests, observations, sample collection)
- Medication requests
- Service requests
- Insurance (payors, contracts, policies, coverage, claims)
- Patient duplicate checking
- Multiple medical code standards

Much of the data model follows **HL7 FHIR**. Facilities are modelled as Service Units and specialities as Medical Departments. ERPNext supplies pharmacy, supplies, purchasing, HR, accounts, and assets. Healthcare documents integrate with Sales Invoice and Payment Entry.

**Entry points:**
- Frappe Desk forms, reports, dashboards, and workspaces under `healthcare/healthcare/`
- A Vue patient portal served at `/patient-portal` (`healthcare/www/`)
- A regional `india` module (ABDM custom fields)

**Branches:** `biograph-fh` is the fork's main branch. It is kept in sync with upstream `earthians/marley` `version-16` through tracked cherry-pick batches (see `wiki/upstream-sync-version-16.md`).
