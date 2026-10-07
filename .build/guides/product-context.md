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

# Product context

**Biograph** (app name `healthcare`, by Tacten / fossibleworks) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' *Marley Health*, with additions on top. It runs as a Frappe app on top of **ERPNext** (`required_apps = ["frappe/erpnext"]`). Much of its data model follows **HL7 FHIR**: Observation, Diagnostic Report, Service Request, Code System/Value Set, and so on.

## Who uses it
- **Clinical staff and administrators** work in Frappe Desk (`app_home = /desk/healthcare`). Their work covers patient registration, outpatient appointments, inpatient admission and medication, clinical procedures, lab tests and sample collection, therapy and rehab plans, nursing tasks, discharge summaries, and insurance payors, contracts and claims.
- **Patients** use the Vue **Patient Portal** (`/patient-portal`). There they book appointments, see diagnostics, and pay fees (consultation and registration).
- ERPNext supplies billing (Sales Invoice, Payment Entry), stock and pharmacy, HR and accounts.

## Key domain concepts
The main records are Patient, Healthcare Practitioner, Patient Appointment, Fee Validity, Healthcare Service Unit (facilities modelled as a tree), Medical Department (specialities), Lab Test and Lab Test Template, Observation, Service Request, Medication Request, Inpatient Record, and Insurance Claim. There are about 139 doctypes under `healthcare/healthcare/doctype/`.

Fork-specific features are documented in `wiki/`:
- block-based therapy appointment booking
- patient duplicate check
- FHIR terminology service
- insurance parity

The `regional/india` module adds ABDM integration (`abdm_request`, `abdm_settings`).
