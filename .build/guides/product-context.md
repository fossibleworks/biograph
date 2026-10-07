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
  - healthcare/regional/india/abdm/utils.py
---

**Biograph** (by Tacten; the package is named `healthcare`) is an open-source **Hospital Information System (HIS)** for clinics, hospitals and other healthcare organisations. It is a fork of earthians' Marley Health, with extra features added on top. It is a **Frappe app that requires ERPNext** (`required_apps = ["frappe/erpnext"]`), and much of its data model follows **HL7 FHIR**.

**Users**
- Desk users (practitioners, nurses, lab staff, billing and admin) work in the Frappe desk. The app's home is `/desk/healthcare`, and the landing page after login is set per role (`on_login` → `auth.set_role_based_home_page`).
- Patients use the **Patient Portal** at `/patient-portal` (role `Patient`), plus web forms for lab tests, prescriptions, appointments and personal details.

**Main feature areas** (from the README and doctypes): patient management and duplicate-patient checks; outpatient flows (Patient Appointment, Patient Encounter, Fee Validity, Practitioner Schedule/Availability, block-based therapy booking); inpatient flows (Inpatient Record, medication orders and entries, Discharge Summary); Clinical Procedures; Rehabilitation and Physiotherapy (Therapy Plan/Type, Exercise); Laboratory (Lab Test, Sample Collection, Observation, Diagnostic Report); medical code standards (Code System/Code Value); insurance (Payor, Contract, Eligibility, Claim); and India-specific ABDM integration under `healthcare/regional/india/abdm`.

**ERPNext integration:** billing goes through ERPNext Sales Invoice and Payment Entry, using an overridden `HealthcareSalesInvoice` class and doc_events. Facilities are mapped as Healthcare Service Units (a tree under Company). Pharmacy, stock, HR and accounts come from ERPNext.

This repository is the **fossibleworks fork** (`fossibleworks/biograph`, integration branch `biograph-fh`). It is periodically synced from upstream `earthians/marley` `version-16`. The rule for those syncs is that fork behaviour wins (see `wiki/upstream-sync-version-16.md`).
