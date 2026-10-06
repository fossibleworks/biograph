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

**Biograph** (Python app name `healthcare`, app title "Biograph", tracked in Build as *fossibleHIS*) is an open-source Hospital Information System (HIS) built by Tacten. It is a fork of earthians' **Marley Health**, with Tacten's own changes on top. It runs as a Frappe app on top of **ERPNext** (`required_apps = ["frappe/erpnext"]`), and much of its data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics and hospitals (desk users) and patients (through the Patient Portal at `/patient-portal`, which requires the `Patient` role).

**Core domains:** Patient management, Patient Appointments and practitioner scheduling (including block-based therapy booking), Outpatient/Inpatient (Inpatient Record, medication orders), Patient Encounters, Clinical Procedures, Rehabilitation/Physiotherapy (Therapy Plans/Sessions), Laboratory (Lab Test, Sample Collection, Observations, Diagnostic Report), Service Requests and Medication Requests, Insurance (payors, contracts, policies, coverage, claims), medical code standards (Code System / Code Value) and patient duplicate detection. Facilities are modelled as **Healthcare Service Units** and specialities as **Medical Departments**. ERPNext supplies billing (Sales Invoice, Payment Entry), stock/pharmacy, HR and accounts. There is India-specific regional code for ABDM (`healthcare/regional/india/abdm`).

**Fork context:** the working branch is `biograph-fh`. Upstream `earthians/marley version-16` is synced in batches, and each batch is recorded in `wiki/upstream-sync-version-16.md`. In conflicts, fork behaviour wins.
