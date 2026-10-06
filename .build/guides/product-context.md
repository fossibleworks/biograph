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
  - pyproject.toml
  - healthcare/hooks.py
  - healthcare/www/patient_portal.py
---

Biograph (by Tacten; the package is still named `healthcare`) is an open-source **hospital information system (HIS)**. It is a fork of earthians' Marley Health with extra features. It runs as a Frappe app on top of ERPNext and adds the healthcare domain to ERPNext. Much of the data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics and hospitals (desk users), and patients through the Vue **Patient Portal** (`/patient-portal`).

**Key feature areas:** patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, rehabilitation and physiotherapy (Therapy Plan/Session, Exercise Type), laboratory and diagnostics (Lab Test, Observation, Sample Collection, Diagnostic Report), medication requests, insurance (Insurance Payor, Contract, Claim, Coverage), fee validity, configurable medical code standards, and healthcare facilities modelled as Service Units, with specialities as Medical Departments. India ABDM regional support is under `healthcare/regional/india/abdm`.

ERPNext supplies the accounting, pharmacy and stock, HR, and purchasing parts. Biograph hooks into Sales Invoice, Payment Entry and Company.

This repo (`fossibleworks/biograph`, main branch `biograph-fh`) is a downstream fork. It is periodically synced from upstream `earthians/marley` `version-16`; the ledger is `wiki/upstream-sync-version-16.md`.
