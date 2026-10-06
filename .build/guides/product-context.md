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
  - wiki/FHIR Terminology Service Parity — Implementation Plan.md
---

**Biograph** (by Tacten / FossibleWorks; the repo calls it fossibleHIS) is an open source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with enhancements. It ships as the Frappe app `healthcare` and adds a health domain to **ERPNext**.

**Who uses it:** healthcare practitioners, clinics and hospitals. Staff work in the Frappe Desk (`app_home = /desk/healthcare`). Patients use a separate **Patient Portal** (a Vue SPA served at `/patient-portal`), where they view appointments, book appointments, see diagnostics and pay.

**Core feature areas:**
- Patient management, including patient duplicate checking
- Outpatient and inpatient management: Patient Appointment, Patient Encounter, Inpatient Record
- Clinical Procedures, Therapy, Rehabilitation and Physiotherapy
- Laboratory and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report
- Medication requests, Service Requests and orders
- Insurance: payors, contracts and claims
- Medical code standards (Code System / Code Value), designed around **HL7 FHIR**
- Facilities modelled as Healthcare Service Units, and specialities as Medical Departments
- Regional: India ABDM integration

ERPNext supplies billing (Sales Invoice), pharmacy and stock, HR, accounts and assets. Biograph hooks into these instead of reimplementing them.
