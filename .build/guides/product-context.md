---
title: Product context — Biograph (fossibleHIS)
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
---

## What it is
Biograph (by Tacten / fossibleworks) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians **Marley Health** with extra features. It is packaged as the Frappe app `healthcare` (`app_title = "Biograph"`), and it brings a healthcare domain into **ERPNext**. Much of the data model follows **HL7 FHIR**: Observation, Service Request, Medication Request, Diagnostic Report, Code System/Code Value.

## Who uses it
- **Clinical and admin staff** in clinics and hospitals: practitioners, nurses, lab staff, front desk and billing. They work in the Frappe Desk (`app_home = /desk/healthcare`).
- **Patients**, through the Vue **Patient Portal** at `/patient-portal`. It requires the `Patient` role. Patients can view appointments, book appointments, see diagnostics and pay.

## Main feature areas
Patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record, Inpatient Medication Order/Entry), clinical procedures, rehabilitation and physiotherapy (Therapy Plan/Session, Exercise), laboratory (Lab Test, Sample Collection, Observation, Diagnostic Report), nursing tasks, insurance (Payor, Contract, Eligibility Plan, Claim), fee validity and packages, medical code standards, and service units and medical departments. Billing uses ERPNext Sales Invoice and Payment Entry through hooks. India-specific ABDM integration lives in `healthcare/regional/india/abdm`.

## Fork context
- The working mainline is `biograph-fh`. Upstream earthians/marley `version-16` is brought in with tracked sync batches; see `wiki/upstream-sync-version-16.md`. When a sync conflicts, **fork behaviour wins**.
