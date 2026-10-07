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
  - pyproject.toml
  - healthcare/healthcare/api/patient_portal.py
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
---

**Biograph by Tacten** (packaged as the Frappe app `healthcare`; this fork is tracked as *fossibleHIS*) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with enhancements. It adds the health domain to **ERPNext**, and much of its data model follows **HL7 FHIR**.

**Who uses it:** hospitals, clinics and individual practitioners. Inside the Frappe Desk the main users are clinical staff, front-desk staff, lab staff and billing staff. Patients use the self-service **Patient Portal** at `/patient-portal`, where they book appointments, pay fees, and see appointments, orders and diagnostic reports.

**Core features:** patient management, outpatient and inpatient care (encounters, admissions, inpatient medication orders and entries), clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions, exercises), laboratory (lab tests, samples, templates, observations, diagnostic reports), insurance (payors, contracts, eligibility plans, claims), configurable medical code standards (Code System, Code Value), healthcare service units, and medical departments. Pharmacy, purchasing, HR, accounts and assets come from ERPNext, which is integrated through hooks on Sales Invoice, Payment Entry and Company.

**Fork-specific features** are documented in `wiki/`: block-based (custom time range) appointment booking, practitioner unavailability, the patient duplicate checker, insurance parity, and FHIR terminology parity. The work now in progress keeps the fork (`biograph-fh`) in sync with upstream `earthians/marley` `version-16` while keeping fork behaviour.
