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
  - pyproject.toml
  - wiki/FHIR Terminology Service Parity — Implementation Plan.md
---

**Biograph** (shown as fossibleHIS in Build; maintained by Tacten / Fossibleworks) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with enhancements. It ships as the Frappe app `healthcare` (`app_title = "Biograph"`) and installs on top of **ERPNext**. Most of its data model follows **HL7 FHIR**.

**Who uses it:** healthcare practitioners, clinics and hospitals. That covers front-desk and billing staff, doctors and nurses (desk UI at `/desk/healthcare`), and patients, who use the Patient Portal at `/patient-portal`.

**Main feature areas** (each is a DocType under `healthcare/healthcare/doctype/`):
- Patient management, including duplicate-patient checks
- Outpatient work: Patient Appointment, Patient Encounter, Fee Validity, practitioner schedules and availability
- Inpatient work: Inpatient Record, medication orders and entries, Nursing Tasks, discharge summaries
- Clinical Procedures, Therapy, Rehabilitation and Physiotherapy (Exercise, Therapy Plan)
- Laboratory and diagnostics: Lab Test, Observation, Diagnostic Report, Sample Collection
- Medical coding: Code System, Code Value, Medical Code standards. There is a FHIR terminology parity plan.
- Insurance: Payor, Contract, Eligibility Plan, Coverage, Claim
- Regional India ABDM integration (`healthcare/regional/india`)
- Billing through ERPNext Sales Invoice and Payment Entry hooks

Pharmacy, purchasing, HR, accounts and assets come from ERPNext itself.
