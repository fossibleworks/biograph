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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - wiki/PATIENT-DUPLICATE-CHECKER-USAGE-DOC.md
  - patient_portal/src/PatientPortal.vue
---

Biograph (by Tacten, maintained in this fork as **fossibleHIS**) is an open-source **Hospital Information System (HIS)**. It is a fork of, and set of enhancements to, Marley Health (earthians). It is shipped as the Frappe app `healthcare` (`app_title = "Biograph"`). It adds the health domain to ERPNext, and most of its data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics, and hospitals (front desk, physicians, nurses, lab staff, billing/insurance staff). Patients use a self-service **Patient Portal** (`/patient-portal`, restricted to the `Patient` role).

**Core capabilities:**
- Patient management, including patient duplicate checks.
- Outpatient and inpatient flows: Patient Appointment (with recurring and block-based therapy booking), Patient Encounter, Inpatient Record, medication orders and entries.
- Clinical Procedures, Rehabilitation/Physiotherapy (Therapy Plan, Exercise), Nursing tasks.
- Laboratory and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report.
- Medical code standards and terminology: Code System, Code Value, FHIR terminology parity work.
- Billing integration with ERPNext Sales Invoice and Payment Entry, fee validity, packages, and insurance (Insurance Payor, Contract, Claim, Eligibility).
- Indian regional support (ABDM) under `healthcare/regional/india`.
- Facilities are modelled as Healthcare Service Units and specialities as Medical Departments.

ERPNext covers pharmacy and supplies, purchasing, HR, accounting, and assets. Biograph builds on those modules and does not re-implement them.
