---
title: Product Context
category: product-context
layer: project
applies_to: []
inclusion: always
binding: reference
source: inferred
evidence:
  - README.md
  - healthcare/hooks.py
  - healthcare/www/patient_portal.py
  - healthcare/patches.txt
  - wiki/insurance-parity-report.md
  - healthcare/regional/india/abdm/utils.py
---

# Product context

**Biograph** (tracked in Build as *fossibleHIS*) is an open-source hospital information system (HIS). It is a fork of Marley Health with extra features, and it ships as the Frappe app `healthcare`. It adds the health domain to ERPNext, so clinics, hospitals and individual practitioners get clinical workflows while billing, stock, HR and accounts stay in ERPNext. Much of the data model follows **HL7 FHIR** (Service Request, Medication Request, Observation, Diagnostic Report, Code System / Code Value).

## Who uses it
- **Front-desk and admin staff**: patient registration, duplicate-patient checks, appointment booking (including block/range booking), fee validity, invoicing and payments.
- **Practitioners and nurses**: Patient Encounters, clinical procedures, observations, lab tests, therapy and rehabilitation plans, inpatient records, discharge summaries.
- **Insurance and billing teams**: Insurance Payor, contracts, coverage, claims.
- **Patients**: a Vue patient portal at `/patient_portal` for appointments, booking, payments and diagnostics.

## Functional areas
The desk workspaces under `healthcare/workspace_sidebar/` are: Healthcare, Outpatient, Inpatient, Diagnostics, Rehabilitation, Insurance and Setup. There is also India-specific ABDM (Ayushman Bharat Digital Mission) integration under `healthcare/regional/india/abdm/`.

## Upstream lineage
The app is still named `healthcare`, the publisher is still "earthians Health Informatics", and several workflows target `earthians/biograph`. The project was rebranded from Marley to Biograph (see the patch `healthcare.patches.v16_0.rebrand_marley_to_biograph`). Recent work keeps "parity" with upstream Marley (see `wiki/insurance-parity-report.md`).
