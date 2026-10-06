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
---

**Biograph** (by Tacten / FossibleWorks; this repo is `fossibleworks/biograph`, also called fossibleHIS) is an open-source **hospital information system (HIS)**. It is a fork of earthians' Marley Health with extra features. It ships as a Frappe app named `healthcare` (app title "Biograph") that adds the health domain to **ERPNext**. Its data model follows **HL7 FHIR** in most places.

**Users:** practitioners, clinics and hospitals (clinical, front-desk, billing and lab staff) working in Frappe Desk at `/desk/healthcare`. Patients use a Vue **Patient Portal** at `/patient-portal`.

**Main features:** patient management, outpatient/inpatient (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, rehab and physiotherapy (therapy plans/sessions), laboratory (Lab Test, Observation, Diagnostic Report), medication requests and inpatient medication orders, insurance (payor, contract, claim), fee validity and packages, and multiple medical code standards (Code System / Code Value). Facilities are modelled as **Healthcare Service Units** and specialities as **Medical Departments**. There is India-specific ABDM integration under `healthcare/regional/india`.

ERPNext supplies pharmacy and stock, purchasing, HR, accounts, and assets. Biograph hooks into ERPNext documents such as Sales Invoice and Payment Entry. Fork features that are documented in `wiki/` include block-based therapy appointment booking, a patient duplicate checker, FHIR terminology service parity, and insurance parity.
