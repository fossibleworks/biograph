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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
---

**Biograph** (by Tacten / fossibleworks; app name `healthcare`, app title "Biograph") is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with enhancements on top. It runs as a Frappe app that adds a healthcare domain to **ERPNext**, and most of its data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics, hospitals and their staff (front desk, nurses, lab, billing), plus **patients** through the Patient Portal (`/patient-portal`, role `Patient`).

**Main features:** patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, rehabilitation and physiotherapy (Therapy Type/Plan, Exercise Type), laboratory (Lab Test, Sample Collection, Observation, Diagnostic Report), medication requests, insurance (Insurance Payor/Contract/Claim), configurable medical code standards, and Healthcare Service Units arranged as a tree. Fork-specific additions include block-based therapy appointment booking, a patient duplicate checker, practitioner availability, and role-based login home pages. Regional code covers India ABDM (`healthcare/regional/india/abdm`).

Pharmacy, purchasing, HR, accounts and assets come from ERPNext. Sales Invoice and Payment Entry are extended through hooks.

The working branch is `biograph-fh`. It is kept at parity with upstream `earthians/marley` `version-16` through a documented cherry-pick ledger. When the fork and upstream conflict, the fork's behaviour wins.
