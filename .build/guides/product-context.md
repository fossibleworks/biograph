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
---

Biograph (by Tacten / fossibleworks, a fork of earthians **Marley Health**, called fossibleHIS in Build) is an open-source **Hospital Information System (HIS)**. It ships as the Frappe app `healthcare` and adds the healthcare domain to **ERPNext**.

**Users:** healthcare practitioners, clinics, and hospitals. Staff use the Frappe Desk (`app_home = /desk/healthcare`). Patients use a separate **Patient Portal**, a Vue SPA served at `/patient-portal` through `healthcare/www`.

**Core features:**
- Patient management and outpatient/inpatient flows: Patient, Patient Appointment, Patient Encounter, Inpatient Record
- Clinical Procedures, Therapy/Rehabilitation and Physiotherapy
- Laboratory: Lab Test, Sample Collection, Observation, Diagnostic Report
- Medication Requests, Service Requests, insurance (payor contracts, coverage, policies)
- Medical code standards (Code System / Code Value), with a design based on **HL7 FHIR**
- Service Units and Medical Departments; regional extensions (`healthcare/regional/india`, ABDM)

ERPNext provides pharmacy and stock, purchasing, HR, accounts, and assets. Billing runs through Sales Invoice, which this app hooks into and overrides.

Fork-specific features are documented in `wiki/`: block-based therapy appointment booking, the patient duplicate checker, insurance parity, and FHIR terminology parity.
