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
  - healthcare/healthcare/api/patient_portal.py
  - wiki/PATIENT-DUPLICATE.md
  - .build/project.yaml
---

# Product context

**Biograph** (by Tacten; this repo is tracked in Build as **fossibleHIS**) is an open-source **hospital information system (HIS)** for healthcare organisations. It forks and extends *Marley Health*. It is installed as a **Frappe app named `healthcare`** on top of **ERPNext** (`required_apps = ["frappe/erpnext"]`).

## What it does
- Patient management, outpatient and inpatient management (Patient Appointment, Inpatient Record, Fee Validity).
- Clinical procedures, rehabilitation and physiotherapy (Therapy Plan/Session, Exercise), laboratory (Lab Test, Lab Test Template), observations, diagnostic reports, and medication requests.
- Insurance: payor contracts, patient insurance policy and coverage, and item insurance eligibility.
- Medical code standards (Code System, Code Value). Much of the design follows **HL7 FHIR**.
- Facilities are modelled as **Healthcare Service Units** and specialities as **Medical Departments**.
- Regional integration: India / ABDM (`healthcare/regional/india/abdm`).
- A **Patient Portal** (Vue SPA served at `/patient-portal`) where patients see appointments, book slots, and pay.
- ERPNext supplies pharmacy, purchasing, HR, accounts, and assets. Billing goes through Sales Invoice hooks.

## Users
Practitioners, front desk, nursing, lab, and billing staff work in Frappe Desk (`app_home = /desk/healthcare`). Patients use the web portal. Role-based home pages are set at login (`on_login` hook).

Feature design notes live in `wiki/`, for example patient duplicate checking, block-based therapy appointment booking, FHIR terminology parity, and insurance parity.
