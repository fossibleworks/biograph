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
  - pyproject.toml
---

**Biograph** (by Tacten, maintained here as **fossibleHIS**, `fossibleworks/biograph`) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health with added features. It ships as the Frappe app `healthcare` and adds a healthcare domain to **ERPNext**. Most of its data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics, hospitals, and their front desk, nursing, lab and billing staff, all working in Frappe Desk. Patients use the Vue **Patient Portal** at `/patient-portal`, which is limited to the `Patient` role.

**Main features:** patient management, outpatient and inpatient care (appointments, encounters, inpatient records, medication orders and entries), clinical procedures, therapy and rehabilitation (therapy plans and sessions, exercises), laboratory work (lab tests, sample collection, observations, diagnostic reports), insurance (payors, contracts, eligibility, claims), fee validity, medical code standards (code systems and values, FHIR terminology), and India ABDM integration. Billing, stock/pharmacy, HR and accounts come from ERPNext. Healthcare documents feed Sales Invoice and Payment Entry through `doc_events`.

Facilities are modelled as **Healthcare Service Units** in a tree. Specialities are modelled as **Medical Departments**.

The fork's branch is `biograph-fh`. It is kept in sync with upstream `earthians/marley` `version-16` by cherry-picking, and the sync is recorded in `wiki/upstream-sync-version-16.md`. The fork's own behaviour always wins over upstream changes.
