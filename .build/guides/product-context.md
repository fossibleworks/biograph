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
  - healthcare/www/patient-portal/index.py
  - patient_portal/src/components/BookAppointmentModel.vue
  - CLAUDE.md
---

**Biograph** (package/app name `healthcare`, branded "fossibleHIS"/Biograph by Tacten) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with additional features. It is a Frappe app that adds a healthcare domain to **ERPNext**. Most of its data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics and hospitals. Front-desk, nursing, lab, billing and admin staff work in Frappe Desk (`/desk/healthcare`). Patients use a separate **Patient Portal** SPA (`/patient-portal`) to book appointments, see diagnostics and pay bills.

**Main feature areas** (from README and doctypes): patient management, including duplicate-patient checking; outpatient and inpatient care (appointments, encounters, admissions, inpatient medication); clinical procedures; rehabilitation and physiotherapy (therapy plans and sessions, exercises, block-based therapy appointment booking); laboratory and diagnostics (lab tests, sample collection, observations, diagnostic reports); medication requests; service requests and orders; insurance (payors, contracts, policies, coverage, claims); configurable medical code standards (Code System / Code Value); service units and medical departments; fee validity and healthcare packages; India-specific ABDM integration (`healthcare/regional/india`, ABDM doctypes).

Pharmacy, purchasing, HR, accounts and assets come from ERPNext. For example, Sales Invoice is overridden by `HealthcareSalesInvoice`.

**Fork context:** the working default branch is `biograph-fh`. The repo is kept in sync with upstream `earthians/marley version-16` by cherry-picking, and each sync is recorded in a ledger at `wiki/upstream-sync-version-16.md`.
