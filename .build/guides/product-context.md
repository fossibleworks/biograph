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
  - patient_portal/src/PatientPortal.vue
---

**Biograph (fossibleHIS)** is an open-source Hospital Information System (HIS) from Tacten. It is a fork of earthians' **Marley Health**, with Tacten's own enhancements. It ships as a Frappe app named `healthcare`, with app title "Biograph", and it requires ERPNext. It adds a healthcare domain to ERPNext.

**Who uses it:** hospitals, clinics and healthcare practitioners. Front-desk, clinical, lab, nursing and billing staff work in Frappe Desk at `/desk/healthcare`. Patients use a self-service **Patient Portal** at `/patient-portal` (a Vue SPA) and Frappe web forms.

**Core feature areas** (139 doctypes under `healthcare/healthcare/doctype/`):
- Patient management, plus patient duplicate checking
- Outpatient appointments, including block-based therapy booking, recurring appointments and practitioner schedules/availability
- Patient Encounters
- Inpatient records and service units
- Clinical procedures
- Rehabilitation and physiotherapy (therapy plans and sessions)
- Laboratory work: Lab Tests, Observations, Diagnostic Reports, Sample Collection
- Medication requests
- Nursing tasks
- Insurance: payors, contracts, policies, coverage, claims
- Medical code standards
- Regional India ABDM integration

Most of the data design follows **HL7 FHIR**. Billing, pharmacy, stock, HR and accounting come from ERPNext. Sales Invoice and Payment Entry are extended through hooks.

The fork tracks upstream `earthians/marley` `version-16` into the fork's main branch `biograph-fh`. Fork behaviour wins when the two conflict (see `wiki/upstream-sync-version-16.md`).
