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
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/regional/india/abdm/test_abdm.py
---

**Biograph** (by Tacten / FossibleWorks; the Build project name is *fossibleHIS*) is an open-source Hospital Information System (HIS). It is a fork of earthians **Marley Health** with extra features. It ships as the Frappe app `healthcare` (`app_title = "Biograph"`) and needs ERPNext installed alongside it.

**Who uses it:** healthcare practitioners, clinics and hospitals. Patients also use it through a self-service **Patient Portal**.

**What it does:**
- Patient management and duplicate-patient checks.
- Outpatient and inpatient workflows: Patient Appointment, Patient Encounter, Inpatient Record.
- Clinical Procedures, Rehabilitation/Physiotherapy (therapy plans, block-based therapy booking), Laboratory and diagnostics (Lab Test, Observation, Diagnostic Report).
- Medication requests, Insurance (payors, contracts, policies, claims), and multiple medical code standards.
- Facilities are modelled as Healthcare Service Units, and specialities as Medical Departments.
- Most of the design follows **HL7 FHIR**. A regional India/ABDM integration lives in `healthcare/regional/india/abdm`.
- It uses ERPNext for billing (Sales Invoice), pharmacy and stock, HR, accounts and assets.

**Entry points:**
- The Desk workspace at `/desk/healthcare`.
- The Vue patient portal served from `healthcare/www/patient_portal.html` and `www/patient-portal/`.
- Whitelisted APIs in `healthcare/healthcare/api/patient_portal.py`.

**Fork-specific design notes** live in `wiki/`, for example block-based therapy appointment booking, patient duplicate checker, insurance parity and FHIR terminology parity.
