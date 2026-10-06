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

**Biograph by Tacten** (packaged here as fossibleHIS, `fossibleworks/biograph`) is an open-source **hospital information system (HIS)**. It is a fork of earthians **Marley Health**, with extra features added on top. It installs as the Frappe app `healthcare` and adds a health domain to **ERPNext**.

**Users:** healthcare practitioners, clinics, hospitals and their admin, billing and nursing staff, who work in the Frappe Desk at `/desk/healthcare`. Patients use a separate **Patient Portal** (Vue SPA at `/patient-portal`) to see appointments, book appointments, view lab or diagnostic orders, and pay.

**Main capabilities** (from the README and the 139 doctypes):
- Patient management, including duplicate-patient checks
- Outpatient care: Patient Appointment, Patient Encounter, Fee Validity, recurring and block-based therapy appointments
- Inpatient care: Inpatient Record, medication orders and entries, service-unit occupancy
- Clinical procedures, rehabilitation and physiotherapy (Therapy Plan, Exercise)
- Laboratory and diagnostics: Lab Test, Observation, Sample Collection, Diagnostic Report
- Insurance: payors, contracts, policies, coverage, claims
- Multiple medical code standards (Code System / Code Value), with a FHIR-inspired design
- Facilities are modelled as Healthcare Service Units and specialities as Medical Departments
- India regional: ABDM integration (`healthcare/regional/india/abdm`)

ERPNext supplies pharmacy and stock, purchasing, HR, accounts, assets and invoicing. Biograph hooks into Sales Invoice, Payment Entry and Company.

**Fork context:** the `biograph-fh` branch keeps itself in parity with upstream earthians/marley `version-16` through cherry-pick sync batches. When upstream and fork behaviour conflict, fork behaviour wins (see `wiki/upstream-sync-version-16.md`).
