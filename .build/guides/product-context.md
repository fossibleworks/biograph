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
  - healthcare/hooks.py
  - healthcare/www/patient_portal.py
---

**Biograph** (package name `healthcare`, version 16.0.x) is an open-source Hospital Information System (HIS) by Tacten / FossibleWorks. It is a fork of earthians **Marley Health** with extra features, and it adds a healthcare domain to **ERPNext** on the **Frappe** framework. Most of its data model follows **HL7 FHIR**.

Who uses it: healthcare practitioners, clinics and hospitals (desk users), plus patients through the **Patient Portal** (`/patient-portal`, a Vue SPA).

Main feature areas:
- Patient management and patient duplicate checking
- Outpatient and inpatient care: Patient Appointment, Patient Encounter, Inpatient Record, Fee Validity
- Clinical Procedures, Therapy, Rehabilitation and Physiotherapy, including block-based therapy appointment booking
- Laboratory and diagnostics: Lab Test, Observation, Diagnostic Report, Sample Collection, Service Request
- Medication requests and orders, Treatment Plans, Nursing checklists
- Insurance: payors, contracts, policies, coverage, claims
- Configurable medical code standards. Facilities are modelled as Healthcare Service Units and specialities as Medical Departments
- Regional: India ABDM integration (`healthcare/regional/india/abdm`)

ERPNext supplies billing (Sales Invoice, Payment Entry), pharmacy and stock, HR, accounts and assets. Healthcare hooks into those doctypes instead of rebuilding them.

This repo, `fossibleworks/biograph` (internally "fossibleHIS"), tracks upstream `earthians/marley` `version-16`. Its own integration branch is `biograph-fh`.
