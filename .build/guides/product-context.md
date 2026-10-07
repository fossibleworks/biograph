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

**Biograph** (app name `healthcare`, branded fossibleHIS / "Biograph - by Tacten") is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health with added features. It runs as a Frappe app on top of ERPNext and adds the healthcare domain to ERPNext. Much of its data model follows **HL7 FHIR**.

**Who uses it:** healthcare practitioners, clinics and hospitals (desk users such as practitioners, nurses, lab staff and billing staff), plus patients through a **Patient Portal** (a Vue SPA served at `/patient_portal`).

**Main feature areas (from the README and the doctype tree):**
- Patient management, with patient duplicate checking (see the `wiki/PATIENT-DUPLICATE*.md` docs)
- Outpatient and inpatient care: Patient Appointment, Patient Encounter, Inpatient Record, block-based therapy appointment booking
- Clinical Procedures, Rehabilitation and Physiotherapy (Therapy Plan, Exercise Type)
- Laboratory and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report, Service Request
- Insurance: payor contracts, policies and coverage
- Configurable Medical Code Standards and FHIR terminology. Facilities are modelled as Healthcare Service Units and specialities as Medical Departments
- Regional customisations, for example `healthcare/regional/india` (ABDM)

Pharmacy, purchasing, HR, accounts and assets come from ERPNext. In `hooks.py`, `required_apps = ["frappe/erpnext"]` and the desk home is `/desk/healthcare`.

**Fork lineage:** upstream is `earthians/marley` (`version-16`), and this fork's working branch is `biograph-fh`. Upstream commits are cherry-picked in using the policy in `wiki/upstream-sync-version-16.md`.
