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

**Biograph** (fossibleHIS, `fossibleworks/biograph`) is an open-source **Hospital Information System (HIS)** from Tacten. It is a fork of **Marley Health** (earthians), with Tacten's own additions on top. It ships as a Frappe app named `healthcare` that runs on top of **ERPNext**. Much of its domain model follows **HL7 FHIR**.

**Who uses it:** healthcare practitioners, clinics and hospitals (desk users such as practitioners, nurses, lab and billing staff), and patients through the **Patient Portal** (`/patient-portal`, Patient role).

**Main feature areas:** patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, rehabilitation and physiotherapy (Therapy Plan/Type), laboratory and diagnostics (Lab Test, Observation, Diagnostic Report, Sample Collection), medication requests, service requests, insurance (Payor, Contract, Policy, Claim), medical code standards, service units as a tree, and medical departments. Billing, pharmacy and stock, HR and accounts come from ERPNext. India-specific ABDM integration lives under `healthcare/regional/india`.

Fork-specific features are documented in `wiki/`: block-based therapy appointment booking, the patient duplicate checker, insurance parity, and FHIR terminology. The fork regularly syncs with upstream Marley `version-16`.
