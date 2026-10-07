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
  - healthcare/healthcare/api/patient_portal.py
---

**Biograph by Tacten** (deployed as *fossibleHIS*) is an open-source **hospital information system (HIS)**. It is a fork of earthians' Marley Health with added features. It ships as a Frappe app named `healthcare` (`app_title = "Biograph"`) and needs ERPNext installed (`required_apps = ["frappe/erpnext"]`).

**Who uses it:** healthcare practitioners, clinics and hospitals. They work in the Frappe Desk at `/desk/healthcare`. Patients use a separate Vue **Patient Portal** served from `healthcare/www/patient_portal.html`, where they can book appointments, pick a department or practitioner, and pay.

**Main feature areas:** patient management, outpatient and inpatient care (appointments, encounters, inpatient records), clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions, exercises), laboratory and diagnostics (lab tests, observations, diagnostic reports, sample collection), medication requests, insurance (payors, contracts, policies, coverage, claims), fee validity and packages, and configurable medical code standards (code systems and values). Most of the data model follows **HL7 FHIR**. Facilities are modelled as *Healthcare Service Units* and specialities as *Medical Departments*. Billing, stock, HR and accounts come from ERPNext through Sales Invoice and Payment Entry hooks.

**Fork-specific work** (documented in `wiki/`): block-based therapy appointment booking, a patient duplicate checker, FHIR terminology-service parity, an insurance parity report, and the upstream sync ledger. There is also India-specific ABDM integration under `healthcare/regional/india/abdm`.
