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
  - .build/project.yaml
---

# Product context

**Biograph** (by Tacten/FossibleWorks) is an open-source Hospital Information System (HIS). It is a fork of, and adds to, earthians **Marley Health**. It ships as the Frappe app `healthcare` (`app_title = "Biograph"`). The Build project for this repo is named **fossibleHIS**.

## What it does
- Adds the healthcare domain to **ERPNext**. Most of the design follows **HL7 FHIR**.
- Core feature areas:
  - Patient management
  - Outpatient and inpatient care (admissions, transfers, discharge, inpatient medication orders and entries)
  - Patient appointments, practitioner schedules and availability, fee validity
  - Clinical procedures, therapy and rehabilitation plans, exercises
  - Lab tests, sample collection, observations and diagnostic reports
  - Medication and medication requests, nursing tasks and checklists
  - Insurance: payors, contracts, eligibility, claims and coverage
  - Medical code standards and FHIR-style code systems and value sets
  - India ABDM integration under `healthcare/regional/india/abdm`
- Facilities are modelled as **Healthcare Service Units** (a tree). Specialities are modelled as **Medical Departments**.
- Billing, pharmacy and stock, HR, accounts and assets come from ERPNext (for example Sales Invoice and Payment Entry hooks).

## Who uses it
- **Hospital and clinic staff** use Frappe Desk. The app home is `/desk/healthcare`, and staff work in workspaces, doctype forms, reports and the patient history and progress pages. Users include practitioners, nurses, lab staff, front desk and billing.
- **Patients** use the **Patient Portal** at `/patient-portal`. It is a Vue SPA where patients view and book appointments, see prescriptions and lab and diagnostic reports, and pay bills.

## Fork context
- This fork's integration branch is `biograph-fh`. Fork changes are layered on top of upstream earthians/marley `version-16`, and upstream commits are cherry-picked in batches. The sync ledger is `wiki/upstream-sync-version-16.md`.
- Fork-specific features are documented in `wiki/`. Examples: block-based therapy appointment booking, the patient duplicate checker, insurance parity, and FHIR terminology service parity.
