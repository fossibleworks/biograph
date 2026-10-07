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
---

**Biograph** (by Tacten, maintained here as the `fossibleworks/biograph` fork, branded fossibleHIS) is an open-source **Hospital Information System (HIS)**. It started as a fork of earthians' *Marley Health* and adds its own enhancements on top. It is a **Frappe app named `healthcare`**. It adds a healthcare domain to **ERPNext** (`required_apps = ["frappe/erpnext"]`), and much of its data model follows **HL7 FHIR**.

**Who uses it:** clinics, hospitals and healthcare practitioners:
- front-desk and admin staff: patient registration, appointments, billing
- clinicians: encounters, procedures, lab tests, observations, therapy
- patients, through a self-service **Patient Portal** at `/patient-portal`

**Main feature areas:**
- Patient management, including duplicate-patient checks
- Outpatient and inpatient management
- Appointments: practitioner schedules and availability, block-based therapy booking, recurring appointments
- Clinical procedures, rehabilitation and physiotherapy
- Laboratory and diagnostics: lab tests, sample collection, observations, diagnostic reports
- Medication requests
- Insurance: payors, contracts and claims
- Medical code standards and FHIR terminology: code systems and value sets
- Healthcare Service Units, set up as a tree
- Medical Departments
- Regional ABDM (India) integration

ERPNext supplies pharmacy and stock, purchasing, HR, accounts, assets and quality. Healthcare documents connect into ERPNext Sales Invoices and Payment Entries for billing.

The desk home is `/desk/healthcare` and the app title is "Biograph". The fork syncs from upstream `earthians/marley` `version-16` into its main branch `biograph-fh`.
