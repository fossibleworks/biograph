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
  - healthcare/healthcare/api/patient_portal.py
---

**Biograph** (by Tacten / FossibleWorks; the Build project is named *fossibleHIS*) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' **Marley Health** with extra features added on top. It ships as the Frappe app `healthcare`, which adds a health domain to **ERPNext**. Most of its data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics, and hospitals (front desk, nursing, lab, billing), plus patients through the patient portal.

**Feature areas:**
- Patient management, including duplicate checking (`wiki/PATIENT-DUPLICATE*.md`)
- Outpatient and inpatient management: Patient Appointment, Patient Encounter, admissions, Healthcare Service Units
- Clinical Procedures, Rehabilitation/Physiotherapy (therapy plans and sessions), Laboratory (Lab Test, Observation, Diagnostic Report, Sample Collection)
- Medication requests and orders, Service Requests, Treatment Plans
- Insurance (payors, contracts, policies, claims) and billing through ERPNext Sales Invoice
- Medical code standards (Code System / Code Value), Medical Departments
- Indian regional features (ABDM) under `healthcare/regional/india`
- A patient portal SPA (`/patient-portal`) for booking appointments and seeing diagnostics and payments

ERPNext supplies pharmacy/stock, purchasing, HR, accounting, and assets. The desk app home is `/desk/healthcare`.

**Fork context:** the working branch `biograph-fh` is synced with upstream `earthians/marley` `version-16` in batches, and each batch is recorded in `wiki/upstream-sync-version-16.md`. When the fork's behaviour and upstream's differ, the fork's behaviour wins.
