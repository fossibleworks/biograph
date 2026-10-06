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

**Biograph** (by Tacten / FossibleWorks; the Build project is named *fossibleHIS*) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' *Marley Health* with added features. It ships as a Frappe app called `healthcare` that installs on top of **ERPNext** (`required_apps = ["frappe/erpnext"]`). Most of its data model follows **HL7 FHIR**.

**Who uses it:** healthcare practitioners, clinics and hospitals. Staff work in the Frappe Desk (`app_home = /desk/healthcare`). Patients use a separate Vue **Patient Portal** (`/patient-portal`) to book appointments, pay bills, and view lab and diagnostic results.

**Main feature areas** (about 139 doctypes under `healthcare/healthcare/doctype/`):
- Patient management, Patient Appointment, Fee Validity, practitioner availability and recurring appointments
- Outpatient encounters and Inpatient Records (admission, discharge, inpatient medication orders and entries, nursing tasks)
- Clinical Procedures, Therapy and Rehabilitation (exercise and therapy plans)
- Laboratory: Lab Test, Sample Collection, Observation, Diagnostic Report
- Medication, Medication Request, Service Request, and Code Systems/Code Values for medical code standards
- Insurance: Payor, Contract, Eligibility Plan, Coverage, Claim
- Regional: India ABDM integration (`healthcare/regional/india/abdm`)
- Patient duplicate checking and block-based therapy appointment booking (fork-specific, documented in `wiki/`)

Facilities are modelled as **Healthcare Service Units** and specialities as **Medical Departments**. Pharmacy, purchasing, HR, accounts and assets come from ERPNext. Billing works through ERPNext **Sales Invoice** and **Payment Entry**, using hooks and an overridden Sales Invoice class.
