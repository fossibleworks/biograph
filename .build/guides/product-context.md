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
  - pyproject.toml
  - healthcare/www/patient_portal.py
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
---

**Biograph** (by Tacten / FossibleWorks; tracked in Build as **fossibleHIS**) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' *Marley Health* with added features. It ships as a Frappe app named `healthcare` that installs on top of **ERPNext**.

**Who uses it:** healthcare practitioners, clinics and hospitals (front desk, clinicians, lab, nursing, billing), plus patients through a self-service **Patient Portal**.

**What it does:**
- Patient management: registration, duplicate checking, medical records, patient history.
- Outpatient and inpatient care: Patient Appointment (including recurring and block-based therapy booking), Patient Encounter, Inpatient Record, discharge summaries.
- Clinical procedures, rehabilitation and physiotherapy (therapy plans, sessions, exercise types), nursing checklists.
- Laboratory and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report.
- Medication requests and service requests (orders).
- Insurance: payors, contracts, policies, coverage, claims.
- Medical coding: Code System, Code Value and multiple medical code standards. The data model follows **HL7 FHIR** concepts.
- Regional support: India **ABDM** integration (`healthcare/regional/india/abdm`).
- Billing goes through ERPNext Sales Invoice and Payment Entry. Pharmacy, stock, HR, accounts and assets come from ERPNext.

The top-level desk navigation is the `Healthcare` module (workspaces, dashboards, number cards, reports). The patient-facing web route is `/patient-portal`, a Vue SPA served from `healthcare/www`.
