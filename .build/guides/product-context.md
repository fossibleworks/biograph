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

Biograph (by Tacten / fossibleworks) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians **Marley Health**, with additions. It is a Frappe app (`app_name = "healthcare"`, `app_title = "Biograph"`) that adds the healthcare domain to **ERPNext**, and it requires `frappe/erpnext`.

**Users:** practitioners, clinics and hospitals. That means clinical staff (practitioners, nurses, lab techs), front desk and billing staff, and patients through the Patient Portal.

**Core feature areas** (from README and doctypes):
- Patient management, outpatient appointments and encounters, inpatient records and admissions
- Clinical procedures, therapy, rehabilitation and physiotherapy, nursing tasks and checklists
- Laboratory (lab tests, samples, templates), observations and diagnostic reports
- Medication requests and inpatient medication orders
- Insurance payors, contracts, eligibility and claims
- Medical code standards and code systems. The data model follows **HL7 FHIR** (Service Request, Observation, Diagnostic Report, Code Value, etc.)
- Facilities are modelled as Healthcare Service Units, and specialities as Medical Departments
- Regional: India ABDM integration (`healthcare/regional/india/abdm`)
- A Patient Portal SPA (`/patient-portal`) for booking appointments, payment and viewing diagnostics

Billing, stock, HR and accounts come from ERPNext (Sales Invoice, Payment Entry, Item and Company hooks).

This fork's integration branch is `biograph-fh`. It is periodically synced from upstream `earthians/marley` `version-16`, and **fork behaviour wins** on conflict.
