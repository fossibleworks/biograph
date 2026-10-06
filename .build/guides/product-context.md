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

Biograph (by Tacten / FossibleWorks; internally called **fossibleHIS**) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with enhancements. It ships as the Frappe app `healthcare`, which brings the health domain into **ERPNext**. Much of the data model follows **HL7 FHIR**: Code System, Code Value, Code Value Set, Observation, Diagnostic Report, Service Request and Medication Request.

**Who uses it**
- Clinics and hospitals: front desk, practitioners, nurses, lab staff, and billing or insurance teams. They work in Frappe Desk under `/desk/healthcare`.
- Patients use the Vue **Patient Portal** at `/patient-portal`, plus web forms for lab tests, prescriptions, appointments and personal details. Portal access requires the `Patient` role.

**Core features**
- Patient management, including duplicate-patient checks.
- Appointments: practitioner schedules, block-based therapy booking, unavailability, fee validity and free follow-ups.
- Outpatient work (Patient Encounter, Vital Signs).
- Inpatient work: Inpatient Record, medication orders and entries, occupancy billing.
- Clinical procedures, therapy and rehabilitation, and nursing tasks.
- Laboratory: Lab Test, samples, Observation, Diagnostic Report.
- Medical coding and terminology.
- Insurance: payors, contracts, eligibility, coverage and claims.
- India-specific ABDM integration under `healthcare/regional/india/abdm`.

Pharmacy, stock, purchasing, HR, accounts and assets come from ERPNext itself. Biograph hooks into Sales Invoice and Payment Entry rather than reimplementing them.

**Branches and upstream**
- The fork's working branch is `biograph-fh`.
- Upstream Marley `version-16` commits are periodically cherry-picked in. The ledger is `wiki/upstream-sync-version-16.md`.
