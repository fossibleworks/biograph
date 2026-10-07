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

# Product context

**Biograph** (by Tacten; the internal name is *fossibleHIS*) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' **Marley Health** with extra features. It ships as a Frappe app named `healthcare` that adds the health domain to **ERPNext**. Most of its data design follows **HL7 FHIR**.

## Who uses it
- **Clinical staff** (practitioners, nurses, lab technicians) and **front-desk/billing staff** at clinics and hospitals. They work in the Frappe Desk at `/desk/healthcare`.
- **Patients**, through a self-service **Patient Portal** (a Vue SPA at `/patient-portal`). Patients can book appointments, see lab/diagnostic results and pay bills.

## Main feature areas
- Patient management: Patient, duplicate-check rules, Patient Medical Record, Patient History page.
- Outpatient: Patient Appointment, Practitioner Schedule and Availability, Fee Validity, Patient Encounter, recurring and block-based therapy appointments.
- Inpatient: Inpatient Record, medication orders and entries, Healthcare Service Units.
- Clinical procedures, rehabilitation and physiotherapy (Therapy Plan/Type/Session), nursing tasks and checklists.
- Lab and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report.
- Medical code standards: Code System, Code Value, Code Value Set (FHIR terminology).
- Insurance: payor contracts, patient insurance policy and coverage, item eligibility.
- Billing through ERPNext Sales Invoice and Payment Entry. Pharmacy, HR, accounts and assets come from ERPNext.
- Regional add-ons: `healthcare/regional/india` (ABDM).

## Fork context
- The working trunk is `biograph-fh`. Upstream marley `version-16` is regularly cherry-picked in, under a "fork intent wins" policy (see `wiki/upstream-sync-version-16.md`).
