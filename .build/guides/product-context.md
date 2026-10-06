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
  - patient_portal/src/components/BookAppointmentModel.vue
---

**Biograph** (by Tacten; packaged as the Frappe app `healthcare`, titled "Biograph" in `hooks.py`) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health with added features. It runs as an app on **Frappe + ERPNext** and adds the healthcare domain to ERPNext. Most of the data model follows **HL7 FHIR**.

**Who uses it:** healthcare practitioners, clinics and hospitals (desk users), plus patients through a self-service **Patient Portal** (`/patient-portal`, a Vue app).

**Main feature areas:** patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, rehabilitation and physiotherapy (Therapy Plan/Type, Exercise), laboratory and diagnostics (Lab Test, Observation, Diagnostic Report, Sample Collection), medication requests, insurance (Insurance Payor, Insurance Claim), and configurable medical code standards (Code System, Code Value). Facilities are modelled as Healthcare Service Units, and specialities as Medical Departments. Fork-specific features include patient duplicate checking and block-based therapy appointment booking, documented in `wiki/`. Indian regional support (ABDM) lives in `healthcare/regional/india`.

Pharmacy, purchasing, HR, accounts and assets come from ERPNext. Billing hooks into ERPNext Sales Invoice and Payment Entry.

This repo (`fossibleworks/biograph`, default branch `biograph-fh`) is a downstream fork. It regularly syncs from upstream `earthians/marley` `version-16` by cherry-picking.
