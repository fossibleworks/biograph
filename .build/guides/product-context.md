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

**Biograph** (by Tacten / fossibleworks; this fork is called fossibleHIS) is an open-source hospital information system (HIS). It is a fork of Marley Health (earthians/marley) with added features. It ships as the Frappe app `healthcare` (`app_title = "Biograph"`). It adds the health domain to ERPNext and needs `frappe/erpnext` to be installed.

**Users:** healthcare practitioners, clinics and hospitals (desk users at `/desk/healthcare`), and patients, who use the Vue patient portal (`/patient-portal`, `www/patient_portal`).

**Main features:** patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions, block-based therapy appointment booking), laboratory and diagnostics (Lab Test, Observation, Diagnostic Report, Sample Collection), medication requests, insurance (payors, contracts, claims), detecting duplicate patients, and medical code standards. Facilities are modelled as Healthcare Service Units and specialities as Medical Departments. Much of the design follows **HL7 FHIR**. ERPNext covers pharmacy, purchasing, HR, accounts and assets.

**Fork context:** the default branch `biograph-fh` is kept close to upstream `earthians/marley version-16` by cherry-picking upstream commits. When fork and upstream conflict, the fork's behaviour wins (see `wiki/upstream-sync-version-16.md`).
