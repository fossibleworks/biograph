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

**Biograph** (by Tacten; a fork with enhancements of earthians' *Marley Health*) is an open-source **Hospital Information System (HIS)**. It ships as the Frappe app `healthcare` and runs on top of **ERPNext**.

**Who uses it:** healthcare practitioners, clinics and hospitals. Patients also use it through a self-service **Patient Portal** (`/patient-portal`, restricted to the `Patient` role).

**What it covers:** patient management, outpatient and inpatient flows (appointments, encounters, inpatient records, medication orders and entries), clinical procedures, rehabilitation and physiotherapy (therapy plans, exercises), laboratory (lab tests, samples, observations, diagnostic reports), insurance (payors, contracts, policies, coverage, claims) and configurable medical code standards. Facilities are modelled as *Healthcare Service Units* (a tree), and specialities as *Medical Departments*. The domain model is largely based on **HL7 FHIR**.

Pharmacy, purchasing, HR, accounts and assets come from ERPNext. Billing goes through ERPNext Sales Invoice and Payment Entry, which this app hooks into. A regional India module (`healthcare/regional/india`) adds ABDM integration.

**This fork:** the working branch is `biograph-fh` in `fossibleworks/biograph`. Fork-specific features are documented in `wiki/`, for example block-based therapy appointment booking, the patient duplicate checker, FHIR terminology parity and insurance parity. The fork is periodically synced with upstream `earthians/marley` `version-16`. In that sync, fork behaviour wins.
