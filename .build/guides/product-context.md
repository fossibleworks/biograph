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

**Biograph** (by Tacten; developed in this repo as fossibleHIS, `fossibleworks/biograph`) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health with added features. It ships as the Frappe app `healthcare` (`app_title = "Biograph"`) and needs ERPNext (`required_apps = ["frappe/erpnext"]`).

**Users:** healthcare practitioners, clinics and hospitals, working in the Frappe Desk. Patients use a separate **Patient Portal** (Vue SPA at `/patient-portal`) to book appointments, pay, and view diagnostics.

**Main domains:** Patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions), laboratory (Lab Test, Observation, Diagnostic Report), medication requests, nursing tasks, insurance (payor contracts, claims, coverage), fee validity, and patient duplicate checking. Facilities map to **Healthcare Service Units** and specialities map to **Medical Departments**. Much of the data model follows **HL7 FHIR** (Service Request, Observation, codification tables, terminology services).

Accounting, pharmacy stock, HR, purchasing and assets come from ERPNext. Healthcare logic hooks into ERPNext doctypes such as Sales Invoice and Payment Entry.

Fork-specific design docs live in `wiki/` (block-based therapy booking, patient duplicate checker, FHIR terminology parity, insurance parity, upstream v16 sync ledger).
