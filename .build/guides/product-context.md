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
  - healthcare/workspace_sidebar/outpatient.json
  - healthcare/www/patient-portal/index.py
  - wiki/insurance-parity-report.md
  - healthcare/regional/india/abdm/utils.py
---

# Biograph (fossibleHIS)

Biograph is an open-source **Hospital Information System (HIS)**. It started as a fork of Marley Health, with further enhancements by Tacten / FossibleWorks. It ships as a **Frappe app** named `healthcare` (app title "Biograph") and runs inside ERPNext. Most of its domain model follows **HL7 FHIR**.

## Who uses it
- **Clinical and administrative staff** at clinics and hospitals: practitioners, nurses, lab staff, front desk and billing. They work in the Frappe Desk UI (`/desk/healthcare`), using workspaces such as Healthcare, Outpatient, Inpatient, Diagnostics, Rehabilitation, Insurance and Setup.
- **Patients** use the Vue-based **Patient Portal** (`/patient-portal`). There they book appointments, view orders and lab results, and pay bills. The portal requires the `Patient` role and a linked active Patient record.

## Key capabilities
- Patient management, including duplicate detection (`wiki/PATIENT-DUPLICATE*.md`)
- Outpatient work: Patient Appointment (slot and block-time booking, recurring appointments, practitioner unavailability), Patient Encounter, Fee Validity
- Inpatient work: Inpatient Record, medication orders and entries, service unit occupancy billing, nursing tasks and checklists
- Clinical procedures, rehabilitation and physiotherapy (Therapy Plan, Exercise)
- Laboratory and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report
- Medication and medication requests, plus Service Requests (FHIR-style orders)
- Insurance: payors, contracts, eligibility plans, coverage and claims
- Medical code standards (Code System, Code Value), aiming at FHIR terminology parity
- India regional support: ABDM integration (`healthcare/regional/india/abdm`)
- Billing goes through ERPNext Sales Invoice and Payment Entry. Pharmacy, HR, accounts and similar functions come from ERPNext.

The app is installed with `bench get-app` and `bench --site <site> install-app healthcare`. It requires `frappe/erpnext`.
