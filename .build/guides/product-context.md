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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
---

Biograph (by Tacten, maintained here as **fossibleHIS** on the `biograph-fh` branch) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' Marley Health, with additional features. It is a Frappe app named `healthcare` (app title "Biograph") that adds the health domain to ERPNext. Most of its design follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics and hospitals (desk users), plus patients through a web **Patient Portal** (`/patient-portal`). In the portal, patients view and book appointments, see diagnostics, and pay fees.

**Feature areas:** patient management, outpatient and inpatient (Inpatient Record, admissions, service units), appointments (including block-based therapy booking, recurring appointments, practitioner availability, fee validity), clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions), laboratory and diagnostics (Lab Test, Observation, Diagnostic Report, Sample Collection), medication requests, clinical notes, insurance (payors, contracts, coverage, claims), medical code standards (Code System / Code Value), and patient duplicate detection. There is also a regional India module for ABDM (Ayushman Bharat Digital Mission).

ERPNext supplies pharmacy and stock, billing (Sales Invoice hooks), HR, accounts and assets. Healthcare facilities are modelled as **Healthcare Service Units** and specialities as **Medical Departments**.
