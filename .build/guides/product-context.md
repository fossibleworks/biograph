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
  - patient_portal/src/PatientPortal.vue
---

**Biograph (fossibleHIS)** is an open-source Hospital Information System (HIS) by Tacten/Fossibleworks. It is a fork of earthians' Marley Health, with extra features. It ships as a Frappe app named `healthcare` (app title "Biograph") and runs on top of ERPNext.

**Users:** healthcare practitioners, clinics and hospitals, meaning front-desk, clinical, lab, nursing and billing staff. Patients use it through a patient portal.

**Core domains:**
- Patient management and registration, including a patient duplicate checker
- Outpatient and inpatient care: Patient Appointment, Patient Encounter, Inpatient Record
- Clinical procedures, therapy and rehabilitation, lab tests, observations, diagnostic reports
- Medication requests, service requests and orders
- Insurance: payors, contracts, policies, coverage, claims
- Medical code standards and code systems, mostly modelled on HL7 FHIR
- Service units (the facility tree) and medical departments

ERPNext supplies pharmacy and stock, purchasing, HR, accounting, assets and quality. The fork adds block-based appointment booking, FHIR terminology work, insurance parity and patient duplicate checks; see `wiki/`.

**Surfaces:**
- The Frappe Desk at `/desk/healthcare`, made of DocType forms, reports, dashboards and the `patient_history` / `patient_progress` pages
- A Vue patient portal at `/patient-portal`, where patients see appointments and diagnostics, book appointments and pay
- India-specific ABDM integration under `healthcare/regional/india`

**Fork model:** the fork's main branch is `biograph-fh`. Upstream `earthians/marley version-16` is cherry-picked in. When upstream and fork conflict, the fork's behaviour wins.
