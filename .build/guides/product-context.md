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

## What Biograph is

Biograph ("by Tacten", shipped as the `healthcare` Frappe app, app title **Biograph**) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians **Marley Health** with extra features. It adds the healthcare domain to **ERPNext** and runs on the **Frappe** framework. Most of its data model follows **HL7 FHIR** concepts, for example Service Request, Observation, Diagnostic Report, Medication Request and Code System/Code Value.

## Users

- **Clinical staff**: practitioners, nurses and lab staff. They use Frappe Desk (`app_home = /desk/healthcare`). Main records are Patient Appointment, Patient Encounter, Inpatient Record, Lab Test, Clinical Procedure, Therapy Plan/Session, Nursing Task and Observation.
- **Admin and billing staff**: they work with Sales Invoice and Payment Entry hooks, Fee Validity, insurance (Payor, Contract, Coverage, Claim) and Healthcare Settings.
- **Patients**: they use the Vue **Patient Portal** at `/patient-portal` (role `Patient`) and web forms for lab tests, prescriptions, appointments and personal details.

## Key feature areas

- Patient management and duplicate checking
- Outpatient and inpatient care
- Appointments, including block-based and recurring booking and practitioner unavailability
- Clinical procedures, rehab and physiotherapy
- Laboratory and observations
- Medication
- Insurance
- Configurable medical code standards
- Service units (tree) and medical departments
- India regional ABDM integration (`healthcare/regional/india/abdm`)

ERPNext provides pharmacy and stock, purchasing, HR, accounts and assets.

## Fork context

This repo (`fossibleworks/biograph`, default branch `biograph-fh`) tracks upstream earthians/marley `version-16`. Upstream syncs are recorded in `wiki/upstream-sync-version-16.md`. The conflict policy is **fork intent wins**.
