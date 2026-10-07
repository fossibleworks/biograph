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

# Product context

**Biograph** (by Tacten / fossibleworks; published as the Frappe app `healthcare`, app title "Biograph") is an open-source **hospital information system (HIS)**. It forks and extends earthians **Marley Health** and is built on **Frappe** and **ERPNext**. Much of the data model follows **HL7 FHIR**.

## Who uses it
- Hospitals, clinics and individual practitioners: front desk, practitioners, nurses, lab staff, billing and insurance teams. They work in the Frappe Desk at `/desk/healthcare`.
- Patients use the **Patient Portal** (Vue SPA served at `/patient-portal`) to view appointments, lab results and prescriptions, book appointments and pay bills.

## Main functional areas
- Patient management, including a patient duplicate checker.
- Outpatient work: appointments, block-based therapy booking, practitioner availability and encounters.
- Inpatient work: admissions, service-unit occupancy, inpatient medication orders and discharge.
- Clinical procedures, rehab and physiotherapy (therapy plans and sessions), lab tests, observations and diagnostic reports.
- Medical code standards and code systems (FHIR terminology), medication requests and service requests.
- Insurance: payors, contracts, policies, coverage and claims.
- Billing through ERPNext Sales Invoice and Payment Entry (hooked via `doc_events` and `override_doctype_class`).
- India regional support: ABDM integration.

ERPNext supplies pharmacy and stock, purchasing, HR, accounts, assets and quality.

## Repo lineage
- This repo, `fossibleworks/biograph`, works on branch `biograph-fh`. It tracks upstream `earthians/marley` `version-16` through a documented cherry-pick sync ledger.
- Fork behaviour wins conflicts with upstream.
