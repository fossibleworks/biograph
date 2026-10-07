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

**Biograph** (by Tacten, distributed here as *fossibleHIS*, repo `fossibleworks/biograph`) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' *Marley Health* with Tacten's additions. It ships as the Frappe app `healthcare` (`app_title = "Biograph"`). It extends **ERPNext** with a healthcare domain and follows **HL7 FHIR** concepts throughout.

**Who uses it:** hospitals, clinics, and healthcare practitioners. Front-desk, clinical, nursing, lab, and billing staff work in the Frappe Desk (`/desk/healthcare`). Patients use a separate **Patient Portal** (`/patient-portal`, a Vue SPA) to book appointments, pay bills, and view diagnostics.

**Core functional areas** (≈139 DocTypes under `healthcare/healthcare/doctype/`):
- Patient management, including duplicate-patient detection and patient history / medical records
- Outpatient appointments: Patient Appointment, Practitioner Availability / schedules, block-based therapy booking, fee validity, reminders
- Inpatient: Inpatient Record, service units, medication orders, discharge summary
- Clinical: Patient Encounter, Clinical Procedure, Clinical Note, Service Request, Medication Request, Observation, Diagnostic Report
- Laboratory: Lab Test, Sample Collection, templates
- Rehabilitation / physiotherapy: Therapy Plan, Therapy Session, exercises
- Medical coding: Code System, Code Value, codification tables (multiple coding standards)
- Insurance: payor contracts, policies, coverage, eligibility, claims
- Billing, through ERPNext Sales Invoice and Payment Entry hooks
- Regional: India ABDM integration (`healthcare/regional/india/abdm`)

ERPNext covers pharmacy/stock, purchasing, HR, accounts, and assets. Biograph does not re-implement them.

**Upstream relationship:** the fork tracks `earthians/marley` `version-16` through cherry-pick sync batches recorded in `wiki/upstream-sync-version-16.md`. The policy is that **fork behaviour wins** in conflicts.
