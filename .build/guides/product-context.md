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

**Biograph** (by Tacten / FossibleWorks; tracked here as *fossibleHIS*) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' **Marley Health** with extra features, and it ships as the Frappe app `healthcare` (app_title `Biograph`). It adds the health domain to **ERPNext**, and much of its data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics and hospitals (desk users at `/desk/healthcare`), plus **patients** through the Patient Portal (`/patient-portal`, restricted to the `Patient` role).

**Core features:** patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, rehabilitation and physiotherapy (Therapy Plan/Type), laboratory and diagnostics (Lab Test, Observation, Diagnostic Report, Sample Collection), medication requests, insurance (payors, contracts, policies, coverage, claims), service requests and orders, and configurable medical code standards. Facilities are modelled as Healthcare Service Units and specialities as Medical Departments. Billing hooks into ERPNext Sales Invoice and Payment Entry. India-specific regional code (ABDM) lives under `healthcare/regional/india`.

**Fork-specific features** are documented in `wiki/`: block-based therapy appointment booking, the patient duplicate checker, FHIR terminology service parity, and insurance parity. The fork regularly syncs upstream `earthians/marley` `version-16` into its main branch `biograph-fh`.
