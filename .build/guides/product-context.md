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
  - pyproject.toml
  - patient_portal/src/PatientPortal.vue
  - wiki/PATIENT-DUPLICATE.md
---

## What Biograph is

Biograph ("Biograph - by Tacten", repo `fossibleworks/biograph`, shipped as **fossibleHIS**) is an open source **Hospital Information System (HIS)**. It is a fork of **Marley Health** with extra features. It is built as a **Frappe app named `healthcare`**, needs **ERPNext** (`required_apps = ["frappe/erpnext"]`), and adds the health domain to ERPNext. Much of the data model follows **HL7 FHIR** (Service Request, Observation, Diagnostic Report, Medication Request, code systems).

## Who uses it

- **Clinical and front-desk staff in the Frappe Desk** (`app_home = "/desk/healthcare"`). Workspaces cover Healthcare, Outpatient, Inpatient, Diagnostics, Rehabilitation, Insurance and Setup (`healthcare/workspace_sidebar/*.json`, `healthcare/desktop_icon/*.json`). Main records include Patient, Patient Appointment, Patient Encounter, Healthcare Practitioner, Healthcare Service Unit, Lab Test, Clinical Procedure, Inpatient Record, Therapy Plan/Session, Observation, Insurance Claim and Medical Code.
- **Patients, through the Patient Portal** (`/patient-portal`, role `Patient`). This is a Vue/frappe-ui SPA where patients book and view appointments and view diagnostics. There are also web forms for lab tests, prescriptions, appointments and personal details.
- **Billing and finance users**: Biograph hooks into ERPNext's Sales Invoice and Payment Entry for billing, insurance claims and fee validity.

## Key feature areas (from README)

Patient management, Outpatient and Inpatient management, Clinical Procedures, Rehabilitation and Physiotherapy, Laboratory/Diagnostics, Insurance, and support for several Medical Code Standards. Facilities are modelled as Service Units and specialities as Medical Departments. ERPNext covers pharmacy and supplies, purchasing, HR, accounts and assets. There is an India regional module for **ABDM** (`healthcare/regional/india/abdm`).

## Domain vocabulary to reuse

Use these terms: Patient, Practitioner (Healthcare Practitioner), Encounter, Appointment, Service Unit, Medical Department, Service Request, Observation, Diagnostic Report, Inpatient Record, Fee Validity, Insurance Payor/Policy/Coverage/Claim. Do not invent synonyms.
