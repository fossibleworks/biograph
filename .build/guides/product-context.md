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

**Biograph** (by Tacten / fossibleworks; app name `healthcare`, branded **fossibleHIS** in Build) is an open-source Hospital Information System (HIS). It is a fork of earthians **Marley Health** with extra features. It adds the healthcare domain to **ERPNext** on the **Frappe** framework, and much of its data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics, and hospitals, meaning clinical staff, front desk, billing, and lab teams who work in Frappe Desk. Patients use a separate **Patient Portal** (Vue SPA at `/patient-portal`) to book appointments, pay bills, and view test reports and prescriptions.

**Key capabilities:** patient management, outpatient and inpatient care, appointments (including block/therapy booking and recurring appointments), clinical procedures, rehabilitation and physiotherapy, lab tests and observations, service requests, medication requests, insurance (payor contracts, coverage, claims), fee validity, a patient duplicate checker, and configurable medical code standards. Facilities are modelled as Service Units and specialities as Medical Departments. Pharmacy, purchasing, HR, accounts, and assets come from ERPNext.

The fork also tracks upstream `earthians/marley` `version-16`. Upstream fixes are cherry-picked onto `biograph-fh`, and fork behaviour always wins (see `wiki/upstream-sync-version-16.md`).
