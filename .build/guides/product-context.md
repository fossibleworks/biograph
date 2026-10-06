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
  - healthcare/www/patient_portal.py
---

**Biograph** (PyPI/app name `healthcare`, app title "Biograph") is an open-source **Hospital Information System (HIS)** built as a Frappe app on top of **ERPNext**. It is Tacten's fork of earthians' Marley Health. This repository (`fossibleworks/biograph`, branded fossibleHIS in Build) is a downstream fork. Its integration branch is `biograph-fh`, and it is periodically synced from upstream `earthians/marley` `version-16`.

**Users:** healthcare practitioners, clinics and hospitals (desk users such as practitioners, nurses, lab staff, billing and admins), plus patients through a self-service **Patient Portal**.

**Main feature areas (Frappe module `Healthcare`, about 139 doctypes):**
- Patient management: Patient, duplicate-check rules, medical records, relations, insurance policies.
- Outpatient: Patient Appointment, including recurring, block-based and therapy appointments, Practitioner Schedule/Availability, Fee Validity, Patient Encounter.
- Inpatient: Inpatient Record, Occupancy, Medication Orders and Entries, Discharge Summary, Nursing Tasks.
- Clinical: Clinical Procedure, Service Request, Medication Request, Observation, Diagnostic Report, Vital Signs, Patient Assessment.
- Lab and diagnostics: Lab Test, Sample Collection, Specimen, Observation Templates.
- Rehab and physio: Therapy Plan, Session and Type, Exercise.
- Insurance: Payor, Contract, Eligibility Plan, Coverage, Claim.
- Terminology: Code System, Code Value, Codification Table. The data model is largely HL7 FHIR-inspired.
- Regional: India ABDM integration (`healthcare/regional/india`).
- Reports: Diagnosis Trends, Lab Test Report, Patient Appointment Analytics and others.

Finance, pharmacy stock, HR and assets come from ERPNext. Billing goes through ERPNext Sales Invoice and Payment Entry, extended in `healthcare/healthcare/custom_doctype/`. The desk home is `/desk/healthcare`. The patient portal is served at `/patient-portal` (`healthcare/www`).
