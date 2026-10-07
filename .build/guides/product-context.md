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

**Biograph (by Tacten)** is an open-source Hospital Information System (HIS). It is a fork of earthians' *Marley Health* with added features. It is shipped as a Frappe app named `healthcare` (app title "Biograph") and requires ERPNext.

**Who uses it:** clinics, hospitals and other healthcare organisations. Users include healthcare practitioners, nurses, front-desk and billing staff, who work in the Frappe Desk at `/desk/healthcare`. Patients use a self-service **Patient Portal** at `/patient-portal`, which needs the `Patient` role.

**What it does:**
- Patient management, including duplicate-patient checks
- Outpatient appointments, including recurring and block-based therapy appointments, practitioner schedules and unavailability
- Inpatient records, encounters, clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions)
- Laboratory: lab tests, sample collection, observations, diagnostic reports
- Medication requests and service requests, medical codes and multiple code standards
- Insurance: payor contracts, policies, coverage, claims
- Healthcare Service Units (a tree of facilities) and Medical Departments
- Billing through ERPNext Sales Invoice and Payment Entry hooks
- Indian regional support (ABDM) under `healthcare/regional/india`

Much of the data model follows **HL7 FHIR**. ERPNext covers pharmacy and stock, purchasing, HR, accounts and assets.

In this fork the integration branch is `biograph-fh`. Work is kept in sync with upstream `earthians/marley` `version-16` using a cherry-pick ledger in `wiki/upstream-sync-version-16.md`.
