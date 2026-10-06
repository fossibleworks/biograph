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

# Product context

**Biograph** (by Tacten / fossibleworks; shipped here as *fossibleHIS*) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with enhancements. It ships as a Frappe app named `healthcare` (`app_title = "Biograph"`) that adds the healthcare domain to **ERPNext**.

## Who uses it
- Hospitals, clinics, and individual healthcare practitioners, working in the Frappe Desk (`/desk/healthcare`).
- Patients, through the **Patient Portal** (`/patient-portal`, a Vue SPA) to book and view appointments and diagnostic reports.

## What it covers
- Patient management, Outpatient / Inpatient (Inpatient Record, medication orders/entries), Clinical Procedures, Rehabilitation / Physiotherapy (therapy plans and sessions, exercises), and Laboratory (Lab Test, Observation, Diagnostic Report).
- Medical code standards (Code System / Code Value), Service Units, Medical Departments, Insurance (payor, contracts, coverage, claims), nursing tasks and checklists, and patient duplicate checking.
- ERPNext supplies pharmacy/stock, purchasing, HR, accounting and billing (Sales Invoice hooks), and assets.
- Much of the data model follows **HL7 FHIR** (Service Request, Medication Request, Observation, Diagnostic Report).
- The fork adds features such as block-based therapy appointment booking and the patient duplicate checker (see `wiki/`).

## Upstream relationship
This fork's integration branch is `biograph-fh`. It is synced from earthians/marley `version-16` by cherry-pick; see `wiki/upstream-sync-version-16.md`. The rule is that fork behaviour wins conflicts.
