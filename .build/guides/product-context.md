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
  - patient_portal/src/PatientPortal.vue
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
---

Biograph (by Tacten; in this fork, **fossibleHIS** at `fossibleworks/biograph`) is an open source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with enhancements. It ships as a Frappe app named `healthcare` (app title "Biograph") that adds the health domain to **ERPNext**. Much of the data model follows **HL7 FHIR**.

**Who uses it:** healthcare practitioners, clinics and hospitals working in the Frappe Desk (`/desk/healthcare`), plus patients using the Vue **Patient Portal** at `/patient-portal`.

**Main feature areas** (each is a set of DocTypes under `healthcare/healthcare/doctype/`):
- Patient management, including the Patient Duplicate Check (see `wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md`)
- Outpatient work: Patient Appointment, Fee Validity, Practitioner Schedules and Availability, recurring and block-based therapy appointments
- Inpatient work: Inpatient Record, admission and discharge, Inpatient Medication Orders, Nursing Tasks
- Clinical Procedures, Rehabilitation and Physiotherapy (Therapy Plans and Sessions, Exercises)
- Laboratory and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report
- Medical coding: Code System, Code Value, configurable Medical Code Standards
- Insurance: Insurance Payor, Contracts, Claims
- Service Requests and Medication Requests (FHIR-style orders)
- Regional: India ABDM integration (`healthcare/regional/india`)

ERPNext supplies billing (Sales Invoice, Payment Entry), stock and pharmacy, HR and accounts. Biograph hooks into those DocTypes and does not reimplement them.
