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

**Biograph** (by Tacten / fossibleworks, called fossibleHIS in Build) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health with added features. It is a Frappe app (Python package `healthcare`, app title "Biograph") that adds the healthcare domain to **ERPNext**.

**Who uses it:** healthcare practitioners, clinics and hospitals. Staff work in the Frappe desk (`app_home = /desk/healthcare`). Patients use a separate **Patient Portal** SPA at `/patient-portal`, where they book appointments, view appointments, diagnostic orders and reports, and pay.

**Key domains:** patient management, outpatient and inpatient care (Patient Appointment, Inpatient Record, Discharge Summary), clinical procedures, rehabilitation and physiotherapy (Therapy Plan/Session), laboratory and diagnostics (Lab Test, Observation, Diagnostic Report, Sample Collection), medication requests, insurance (payors, contracts, policies, coverage), and medical code standards (Code System / Code Value). Facilities are modelled as Service Units and specialities as Medical Departments. Most of the data design follows **HL7 FHIR**. ERPNext supplies billing (Sales Invoice, Payment Entry), stock and pharmacy, HR and accounts.

**Regional:** India-specific code (ABDM) is in `healthcare/regional/india` and the ABDM doctypes.

**Fork context:** the working branch is `biograph-fh`. It is kept in sync with upstream `earthians/marley` `version-16` through a cherry-pick ledger (`wiki/upstream-sync-version-16.md`). Fork behaviour always wins over upstream.
