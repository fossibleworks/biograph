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

**Biograph (fossibleHIS) by Tacten** is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' *Marley Health* with added features, and it ships as the Frappe app `healthcare` (app title "Biograph").

It adds the healthcare domain to **ERPNext**: patient management, outpatient and inpatient care, clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions), lab and diagnostic reports, observations, medication requests, insurance (payors, contracts, policies, coverage), fee validity and billing through ERPNext Sales Invoices. Much of the data model follows **HL7 FHIR**, for example Service Request, Observation and Diagnostic Report.

**Users:**
- Clinic and hospital staff (practitioners, nurses, front desk, lab, billing) work in the Frappe Desk at `/desk/healthcare`.
- Patients use the **Patient Portal**, a Vue SPA served at `/patient-portal`, to view and book appointments and see diagnostic reports.

ERPNext supplies pharmacy and stock, purchasing, HR, accounts and assets.

This fork's own work so far:
- block-based therapy appointment booking
- patient duplicate checking
- insurance parity
- FHIR terminology parity
- periodic syncs from upstream marley `version-16` (see `wiki/`)
