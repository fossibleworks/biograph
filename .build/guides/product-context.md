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

Biograph (by Tacten; packaged as the Frappe app `healthcare` and tracked in Build as **fossibleHIS**) is an open-source **hospital information system (HIS)**. It is a fork of earthians' Marley Health with extra features added. It runs as a Frappe app on top of **ERPNext** and adds a healthcare domain to it. Much of the data model follows **HL7 FHIR**.

**Who uses it:** hospitals, clinics and healthcare practitioners (desk users), plus patients through a Patient Portal.

**Main feature areas:**
- Patient management, Outpatient and Inpatient management (Patient Appointment, Patient Encounter, Inpatient Record)
- Clinical Procedures, Rehabilitation and Physiotherapy (Therapy Plan, Therapy Type, Exercise)
- Laboratory and diagnostics (Lab Test, Sample Collection, Observation, Diagnostic Report)
- Medication Requests and Service Requests, Medical Codes (several coding standards), Insurance (payors, contracts, coverage, claims)
- Healthcare Service Units (facility tree) and Medical Departments
- India regional support: ABDM integration (`healthcare/regional/india/abdm`)
- Patient Portal (a Vue SPA at `/patient-portal`) for booking appointments, payments, and viewing appointments, prescriptions and diagnostic reports

ERPNext supplies pharmacy and stock, purchasing, HR, accounts, assets and quality. The app hooks into Sales Invoice, Payment Entry and Company.

**Fork context:** this fork's main branch is `biograph-fh`. It is regularly synced with upstream `earthians/marley` (`version-16`). See `wiki/upstream-sync-version-16.md`.
