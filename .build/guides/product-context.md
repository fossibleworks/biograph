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
  - healthcare/www/patient_portal.py
---

Biograph (by Tacten, maintained in this fork as **fossibleHIS** by fossibleworks) is an open-source Hospital Information System (HIS) for healthcare organisations. It is a fork of earthians' Marley Health, with additions. It ships as a Frappe app named `healthcare` that adds the health domain to ERPNext. Its design largely follows HL7 FHIR.

**Who uses it:** healthcare practitioners, clinics, and hospitals, mostly working in the Frappe Desk at `/desk/healthcare`. Patients use a separate Vue **Patient Portal** at `/patient-portal` to book appointments, view diagnostics, and pay.

**Core feature areas:** patient management, outpatient and inpatient management (Patient Appointment, Inpatient Record), clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions), laboratory management (Lab Test, Observation, Diagnostic Report), medication requests, insurance payors and claims, medical code standards (Code System, Code Value), service units, and medical departments. Pharmacy, purchasing, HR, and accounting come from ERPNext, which is a required app. There is a regional India module for ABDM. Fork-specific work is described in `wiki/`, including block-based therapy appointment booking, the patient duplicate checker, a FHIR terminology service, and insurance parity.

**Branch context:** the fork's main branch is `biograph-fh`. It is being synced with upstream `earthians/marley` `version-16` (see `wiki/upstream-sync-version-16.md`). Conflict policy: fork behaviour wins.
