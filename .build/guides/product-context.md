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
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
---

**Biograph (by Tacten)**, also called fossibleHIS, is an open-source Hospital Information System (HIS). It is a fork of earthians' Marley Health with extra features. It ships as a Frappe app named `healthcare` (app title "Biograph") that adds a healthcare domain to ERPNext. Much of the data model follows HL7 FHIR.

**Users:** healthcare practitioners, nurses, lab staff, clinic and hospital administrators (Frappe Desk at `/desk/healthcare`), and patients (Vue patient portal at `/patient-portal`).

**Key capabilities:** patient management, outpatient and inpatient management (appointments, encounters, admissions/discharge), clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions), laboratory and diagnostics (lab tests, observations, diagnostic reports), medication requests, nursing tasks, insurance (payors, contracts, claims), fee validity, medical code standards (code systems and values), and ABDM integration for India. Facilities map to Healthcare Service Units and specialities map to Medical Departments.

ERPNext supplies pharmacy and stock, purchasing, HR, accounts, and assets. Fork-specific features are documented in `wiki/`: block-based appointment booking, patient duplicate checking, FHIR terminology parity, and insurance parity.
