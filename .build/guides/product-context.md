---
title: Product Context
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

**Biograph (by Tacten)** is an open-source Hospital Information System (HIS) for healthcare organisations of any size. It is a fork of earthians' Marley Health with added features, and it ships as the Frappe app `healthcare` (app title "Biograph"). It brings the health domain into ERPNext. Much of the data model follows **HL7 FHIR** (Service Request, Observation, Diagnostic Report, Code System / Code Value).

**Who uses it:** practitioners, clinics and hospitals. Clinical and front-desk staff work in Frappe Desk at `/desk/healthcare`. Patients use a Vue **Patient Portal** to view appointments, book appointments and pay bills.

**Core feature areas:** patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, rehabilitation and physiotherapy (Therapy Plan / Session), laboratory (Lab Test, Sample Collection, Observation), medication requests, insurance (payors, contracts, policies, coverage, claims), fee validity, configurable medical code standards, Healthcare Service Units, and Medical Departments. India-specific ABDM integration lives under `regional/india`.

**Inherited from ERPNext:** pharmacy and stock, purchasing, HR, accounts (Sales Invoice and Payment Entry are hooked), and assets.

This fork's integration branch is `biograph-fh` (repo `fossibleworks/biograph`). Upstream changes from `earthians/marley version-16` are synced in following the ledger in `wiki/upstream-sync-version-16.md`.
