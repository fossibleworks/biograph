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
  - pyproject.toml
  - healthcare/hooks.py
---

# Product context

**Biograph** (by Tacten / fossibleworks; repo name `fossibleworks/biograph`, Build project "fossibleHIS") is an open-source **Hospital Information System (HIS)**. It is a fork of, and adds to, earthians' **Marley Health**. It ships as the Frappe app `healthcare`, which adds a health domain to **ERPNext**.

## Who uses it
- **Clinical staff**: healthcare practitioners, nurses, and lab, therapy and inpatient staff. They work in Frappe Desk (`app_home = /desk/healthcare`).
- **Clinic and hospital administrators**: set up service units, medical departments, insurance payors, billing and settings.
- **Patients**: use the Vue **Patient Portal** (`/patient-portal`) to book appointments, view diagnostics and pay.

## What it does
- Patient management, outpatient and inpatient management, appointments (including block-based therapy booking and practitioner availability), clinical procedures, rehabilitation and physiotherapy, lab tests, observations, diagnostic reports, medication requests, nursing tasks, insurance claims, and patient duplicate detection.
- Supports several medical code standards (Code System, Code Value). Much of the design follows **HL7 FHIR**.
- Healthcare facilities are modelled as **Healthcare Service Units** and specialities as **Medical Departments**.
- ERPNext supplies pharmacy, stock, purchasing, HR, accounts and billing. The app overrides `Sales Invoice`.
- India regional features (ABDM) live under `healthcare/regional/india`.

## Upstream relationship
Biograph-specific work lives on the `biograph-fh` branch. Upstream earthians/marley commits are periodically cherry-picked in, and the fork's behaviour wins on conflicts (see `wiki/upstream-sync-version-16.md`).
