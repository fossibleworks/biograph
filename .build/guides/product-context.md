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

**Biograph** (packaged as the Frappe app `healthcare`, tracked in Build as *fossibleHIS*) is an open-source hospital information system (HIS) maintained by Tacten/Fossibleworks. It is a fork of earthians' **Marley Health** with extra features added on top.

- **What it does:** adds the healthcare domain to ERPNext. That covers patient management, outpatient and inpatient care (appointments, admissions, inpatient medication orders and entries), clinical procedures, rehabilitation and physiotherapy (therapy plans, exercises), laboratory and diagnostics (lab tests, observations, diagnostic reports), medical code standards (Code System, Code Value), insurance (payors, contracts, policies, claims) and fee validity. Facilities are modelled as **Healthcare Service Units** and specialities as **Medical Departments**. Much of the data design follows **HL7 FHIR**, for example Service Request, Medication Request, Observation and Diagnostic Report.
- **Who uses it:** practitioners, clinics and hospitals work in the Frappe desk (`app_home = /desk/healthcare`). Patients use a Vue **Patient Portal** to book appointments, view orders and results, and pay bills.
- **ERPNext integration:** pharmacy and stock, purchasing, HR, accounts and billing (Sales Invoice, Payment Entry hooks), assets and quality all come from ERPNext.
- **Regional:** India ABDM integration lives in `healthcare/regional/india/abdm` (ABDM Settings and ABDM Request doctypes).
- **Fork-specific work** is documented in `wiki/`: block-based therapy appointment booking, the patient duplicate checker, FHIR terminology parity, insurance parity, and the upstream sync ledger.
