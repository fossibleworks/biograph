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

## What Biograph is

Biograph, by Tacten, is an open-source **hospital information system (HIS)**. It is a fork of earthians' Marley Health, with additions. It ships as a Frappe app named `healthcare` (app_title "Biograph") that adds a health domain to **ERPNext**. Much of the data model follows **HL7 FHIR**.

## Who uses it

- Clinics, hospitals and healthcare practitioners use the Frappe desk at `/desk/healthcare`.
- Patients use the **Patient Portal** at `/patient-portal`. It is a Vue SPA that patients use to book and view appointments, view diagnostic reports and pay.

## Feature areas (by doctype / module)

- Patient management, including a patient duplicate checker (see `wiki/PATIENT-DUPLICATE*.md`).
- Outpatient and inpatient care, Patient Appointment (with recurring and block-based therapy booking) and Patient Encounter.
- Clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions).
- Laboratory: lab tests, sample collection, observations and diagnostic reports.
- Medical code standards, service units and medical departments.
- Insurance and billing, built on ERPNext Sales Invoice (overridden as `HealthcareSalesInvoice`) and Payment Entry.

Pharmacy, purchasing, HR, accounts and assets come from ERPNext itself. Do not re-implement them in this app.

## Fork context

This repo is `fossibleworks/biograph`. Its integration branch is `biograph-fh`. It is kept in sync with upstream `earthians/marley` `version-16` by cherry-picking, and the ledger is in `wiki/upstream-sync-version-16.md`. When syncing, the policy is **fork intent wins**.
