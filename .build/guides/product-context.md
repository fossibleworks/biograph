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

**Biograph** (by Tacten / fossibleworks; the internal Build name is *fossibleHIS*) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health with extra features added. It ships as a Frappe app named `healthcare` that adds a healthcare domain to **ERPNext**.

**Who uses it:** healthcare practitioners, clinics and hospitals. Patients use the separate **Patient Portal** web UI (`/patient-portal`).

**Main capabilities:**
- Patient management and patient duplicate checking
- Outpatient and inpatient care: appointments, block/time-slot booking, encounters, admissions
- Clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions), nursing tasks
- Laboratory and diagnostics: lab tests, observations, sample collection, diagnostic reports
- Medical code standards (Code System / Code Value, FHIR terminology parity work)
- Insurance payors, contracts and claims
- Healthcare billing through ERPNext Sales Invoice and Payment Entry

Much of the data model follows **HL7 FHIR**. Pharmacy, purchasing, HR, accounts and assets come from ERPNext itself.

**Branch model:** the fork's working branch is `biograph-fh`. It is synced from upstream `earthians/marley` `version-16`, and that sync is tracked in `wiki/upstream-sync-version-16.md`.
