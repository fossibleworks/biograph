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
  - healthcare/www/patient_portal.py
---

Biograph by Tacten is an open-source hospital information system (HIS). It is a fork of Marley Health (earthians) with added features. It runs as a Frappe app (`app_name = "healthcare"`, `app_title = "Biograph"`) and needs ERPNext installed (`required_apps = ["frappe/erpnext"]`). Most of the domain model follows HL7 FHIR.

**Who uses it:** healthcare practitioners, clinics and hospitals. Staff work in the Frappe Desk at `/desk/healthcare`. Patients use a separate Vue patient portal served at `/patient-portal`, where they book and view appointments and see diagnostic reports.

**Main features:** patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record, medication orders), clinical procedures, rehabilitation and physiotherapy (therapy plans and exercises), laboratory (Lab Test, Observation, Diagnostic Report), insurance (payors, contracts, eligibility, claims), configurable medical code standards (Code System / Code Value), Service Units and Medical Departments, and India-specific regional code under `healthcare/regional/india` (ABDM). ERPNext covers billing (Sales Invoice), pharmacy stock, HR, and accounts.

**Fork context:** `biograph-fh` is this fork's integration branch. It is periodically synced with upstream `earthians/marley` `version-16`. The rule for those syncs is that fork behaviour wins (see `wiki/upstream-sync-version-16.md`). The repo also has fork-specific design docs, for example block-based therapy appointment booking and the patient duplicate checker.
