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

# Biograph (fossibleHIS)

Biograph by Tacten is an open-source **Hospital Information System (HIS)** shipped as the Frappe app `healthcare` (app_title `Biograph`). It is a fork of earthians' Marley Health and adds the health domain to **ERPNext**; much of its data model follows **HL7 FHIR**.

**Users:** practitioners, clinics and hospitals (front desk, nurses, doctors, lab staff, billing and accounts). Patients use a Vue **patient portal** (`/patient-portal`) to book appointments, pay and view diagnostic reports.

**Main feature areas:**
- Patient management and duplicate checking
- Outpatient work: Patient Appointment, Patient Encounter, Fee Validity, block-based therapy appointment booking
- Inpatient work: Inpatient Record, medication orders and entries, service-unit occupancy billing
- Clinical Procedures, Rehabilitation and Physiotherapy (Therapy Plan/Session, Exercise)
- Laboratory and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report
- Service Requests and Medication Requests, medical code systems (Code System, Code Value), insurance (Insurance Payor/Claim)
- Regional: India ABDM integration (`healthcare/regional/india`)
- ERPNext supplies billing (Sales Invoice, Payment Entry), stock, HR and accounts.

The fork's integration branch is `biograph-fh`. It is regularly synced with upstream `earthians/marley` `version-16` (see `wiki/upstream-sync-version-16.md`), and fork behaviour wins conflicts.
