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
  - patient_portal/src/components/BookAppointmentModel.vue
---

**Biograph** (by Tacten / FossibleWorks; internally `fossibleHIS`) is an open-source **hospital information system (HIS)**. It is a fork of Marley Health (earthians `healthcare` app) with extra features. It installs as the Frappe app `healthcare` (`app_title = "Biograph"`) on top of **ERPNext**, and ERPNext is a required app.

**Users:** healthcare practitioners, clinics, hospitals, and their administrative, billing, and insurance staff. Patients use a separate **Patient Portal** (Vue SPA at `/patient-portal`) to book appointments, pay, and view diagnostic reports.

**Core domains** are implemented as DocTypes under the single `Healthcare` module:
- Patient management, including duplicate-patient checking
- Outpatient appointments, including recurring and block-based therapy booking, and practitioner availability/unavailability
- Inpatient records, discharge summaries, and nursing checklists
- Clinical procedures, rehabilitation, physiotherapy (therapy plans/sessions, exercises), and treatment plans
- Laboratory work: lab tests, sample collection, observations, diagnostic reports
- Medication requests and drug interactions
- Insurance: payors, contracts, policies, coverage, claims
- Fee validity and invoicing through ERPNext Sales Invoice and Payment Entry
- Medical code standards and FHIR-style terminology (code systems, value sets)
- Indian regional ABDM integration (`healthcare/regional/india/abdm`)

The design is largely based on **HL7 FHIR**. ERPNext provides pharmacy and stock, purchasing, HR, accounts, and assets.

This repo (`fossibleworks/biograph`, default branch `biograph-fh`) also periodically syncs upstream `earthians/marley` `version-16`. The rule for those syncs: **fork behaviour wins** on conflicts.
