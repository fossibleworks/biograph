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
  - healthcare/hooks.py
  - pyproject.toml
  - healthcare/www/patient_portal.py
---

**Biograph by Tacten** is an open-source hospital information system (HIS) for healthcare organisations of any size. It is a fork of Marley Health (earthians) with added features. It is a Frappe app (Python package `healthcare`, app title `Biograph`) that adds the healthcare domain to ERPNext, and ERPNext is a required app. Much of the design follows HL7 FHIR.

**Users:** healthcare practitioners, clinics and hospitals. They work in the Frappe desk at `/desk/healthcare`. Patients use a separate Vue patient portal served at `/patient-portal`.

**Main feature areas:**
- Patient management and patient duplicate checking
- Outpatient and inpatient management: appointments, encounters, admissions, service units
- Clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions)
- Laboratory work: lab tests, sample collection, observations and diagnostic reports
- Medical code standards (code systems and code values) and FHIR terminology
- Insurance: payors, contracts, policies and coverage
- Indian regional features (ABDM)

Pharmacy, purchasing, HR, accounts and assets come from ERPNext. The product is installed with `bench get-app` and `bench --site <site> install-app healthcare`.

**Fork context:** this repo (`fossibleworks/biograph`, default branch `biograph-fh`) is periodically synced with upstream `earthians/marley` `version-16`. When fork behaviour conflicts with an upstream change, fork behaviour wins (see `wiki/upstream-sync-version-16.md`).
