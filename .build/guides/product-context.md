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
  - healthcare/workspace_sidebar/outpatient.json
  - patient_portal/src/components/BookAppointmentModel.vue
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
---

**Biograph** (fossibleHIS, by Tacten) is an open-source **Hospital Information System (HIS)**. It started as a fork of Marley Health and adds its own features. It ships as a Frappe app named `healthcare` (app title "Biograph") that adds the health domain to **ERPNext**. Most of the data model follows **HL7 FHIR**. It has observations, diagnostic reports, service requests, code systems and value sets.

**Users:** clinics, hospitals and healthcare practitioners. Staff such as practitioners, nurses, lab and billing staff work in the Frappe Desk UI. Patients use a self-service **Patient Portal** (a Vue SPA served at `/patient-portal`) to book appointments, view diagnostics and pay.

**Main areas** (Desk workspaces in `healthcare/workspace_sidebar/`): Healthcare, Outpatient, Inpatient, Diagnostics (lab tests, sample collection, observations), Rehabilitation and physiotherapy (therapy plans and sessions), Insurance (payors, contracts, policies, coverage, claims) and Setup. Other features include:
- multiple medical code standards
- service units and medical departments
- fee validity
- packages
- patient duplicate checking
- block-based therapy appointment booking
- India ABDM integration (`healthcare/regional/india/abdm`)

Pharmacy, purchasing, HR, accounts and assets come from ERPNext. Billing goes through ERPNext Sales Invoice and Payment Entry.
