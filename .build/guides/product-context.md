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

**Biograph** (Python package `healthcare`, app title "Biograph") is an open-source Hospital Information System (HIS) by Tacten. It is a fork of earthians' Marley Health with added features, built as a **Frappe app on top of ERPNext**. Much of its domain model follows **HL7 FHIR** (for example Observation, Service Request, Medication Request, Diagnostic Report, Code System and Code Value).

**Who uses it**
- Clinic and hospital staff use the Frappe Desk at `/desk/healthcare`: practitioners, nurses, lab technicians, front desk and billing.
- Patients use the **Patient Portal** at `/patient-portal`, a Vue SPA where they book appointments, pay bills and view diagnostics. Logins with the `Patient` role go there.

**Main feature areas** (about 139 DocTypes under `healthcare/healthcare/doctype/`)
- Patient management, including duplicate-patient checks
- Outpatient care: Patient Appointment, Patient Encounter, Fee Validity, Practitioner Schedule and Availability
- Inpatient care: Inpatient Record, Inpatient Medication Order and Entry, Discharge Summary
- Clinical Procedures, Therapy and Rehabilitation (Therapy Plan, Exercise), and Nursing Tasks
- Laboratory: Lab Test, Sample Collection, Observation, Diagnostic Report
- Medication and prescriptions, and medical coding (Code System, Code Value)
- Insurance: Payor, Contract, Eligibility, Claim, Coverage
- Billing through ERPNext Sales Invoice and Payment Entry hooks
- India regional ABDM integration (`healthcare/regional/india`)

ERPNext provides pharmacy and stock, accounts, HR and assets. The product docs are hosted externally on DeepWiki. Feature design and usage notes live in `wiki/`.
