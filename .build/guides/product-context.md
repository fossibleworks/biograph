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

**Biograph** (app name `healthcare`, app title "Biograph") is an open-source Hospital Information System (HIS) built on Frappe and ERPNext. It is a fork of earthians' Marley Health, maintained by Tacten; this repo (`fossibleworks/biograph`, branch `biograph-fh`) is a downstream fork of that.

**Users:** healthcare practitioners, clinics and hospitals (desk users such as practitioners, nurses, lab staff and billing staff), plus patients, who use a Vue patient portal at `/patient-portal`.

**Main feature areas:**
- Patient management, Patient Appointments, Patient Encounters
- Outpatient and inpatient care: Inpatient Record, inpatient medication orders and entries, Discharge Summary
- Clinical Procedures, Therapy / Rehabilitation and Physiotherapy (exercises, therapy plans)
- Laboratory: Lab Test, Sample Collection, Observation, Diagnostic Report
- Medication and Medication Request, Service Requests, Nursing Tasks
- Insurance: Insurance Payor, contracts, eligibility, Insurance Claim
- Medical coding: Code System, Code Value. The design is based on HL7 FHIR.
- Facilities are modelled as Healthcare Service Units, and specialities as Medical Departments
- India regional support (ABDM) under `healthcare/regional/india`

It relies on ERPNext for billing (Sales Invoice, Payment Entry), stock, accounts, HR and so on. In-repo feature docs (block-based therapy booking, patient duplicate checking, insurance parity, FHIR terminology) live in `wiki/`.
