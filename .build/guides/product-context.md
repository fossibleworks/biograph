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
  - healthcare/www/patient_portal.html
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
---

**Biograph** (by Tacten / fossibleworks; the repo is tracked in Build as *fossibleHIS*) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with enhancements. It ships as the Frappe app `healthcare` (`app_title = "Biograph"`) and depends on ERPNext (`required_apps = ["frappe/erpnext"]`).

**Who uses it:** healthcare practitioners, clinics and hospitals, working in the Frappe desk at `/desk/healthcare`. Patients use the self-service **Patient Portal** (`/patient-portal`, a Vue SPA).

**Main features:**
- Patient management, including duplicate-patient detection (see `wiki/PATIENT-DUPLICATE*.md`)
- Outpatient appointments: Patient Appointment, fee validity, practitioner schedules and availability, block-based therapy booking
- Inpatient: Inpatient Record, medication orders and entries, nursing tasks and checklists
- Clinical Procedures, Rehabilitation/Physiotherapy (therapy plans, exercises), Laboratory (Lab Test, Sample Collection, Observation, Diagnostic Report)
- Medical coding: Code System, Code Value. The design follows **HL7 FHIR** (Service Request, Medication Request, Observation, and so on)
- Insurance: Payor, Payor Contract, Eligibility Plan, Patient Insurance Coverage/Policy, Insurance Claim
- Billing through ERPNext (Sales Invoice override, Payment Entry hooks)
- India-specific ABDM integration under `healthcare/regional/india/abdm`

ERPNext supplies pharmacy/stock, purchasing, HR, accounts and assets. Biograph adds the health domain on top of these.
