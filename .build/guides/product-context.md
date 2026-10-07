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

**Biograph** (by Tacten / fossibleworks; the Build project is called fossibleHIS) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health with added features. It ships as a **Frappe app named `healthcare`** that adds a healthcare domain to **ERPNext**. Most of the domain model follows **HL7 FHIR**.

**Who uses it:** healthcare practitioners, clinics and hospitals. In-app roles include practitioners, nurses and lab staff. Patients use a web **Patient Portal** (`/patient-portal`, role `Patient`).

**Main feature areas:**
- Patient management, and outpatient/inpatient management (Patient Appointment, Patient Encounter, Inpatient Record)
- Clinical procedures, therapy/rehabilitation/physiotherapy, and nursing checklists
- Laboratory and diagnostics (Lab Test, Sample Collection, Observation, Diagnostic Report)
- Medication requests and service requests (orders)
- Medical code standards, codification, and FHIR terminology/code systems
- Insurance: payors, contracts, policies, coverage, claims
- Billing through ERPNext Sales Invoice and Payment Entry hooks, plus fee validity
- Regional: India ABDM integration (`healthcare/regional/india`)
- Fork-specific features, documented in `wiki/`: block-based therapy appointment booking, patient duplicate checking, practitioner availability

From ERPNext the product also gets pharmacy and stock, purchasing, HR, accounts, assets and quality. The desk home is `/desk/healthcare` (app title "Biograph").

**Upstream relationship:** the fork's working branch is `biograph-fh`. It is synced periodically from `earthians/marley` `version-16` by cherry-picking. The rule is that fork behaviour always wins. See `wiki/upstream-sync-version-16.md`.
