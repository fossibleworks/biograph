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
  - healthcare/healthcare/api/patient_portal.py
  - wiki/BLOCK-APPOINTMENT-BOOKING-USAGE.md
  - wiki/insurance-parity-report.md
---

## What Biograph is

Biograph ("fossibleHIS" in this repo's Build setup) is an open-source **hospital information system (HIS)** maintained by Tacten / FossibleWorks. It is a fork of Marley Health (earthians) with added features. It ships as a **Frappe app named `healthcare`** that depends on ERPNext (`required_apps = ["frappe/erpnext"]`). Inside Frappe the app title is "Biograph" and its home route is `/desk/healthcare`. Much of the data model follows **HL7 FHIR**.

## Who uses it

- **Clinical staff**: practitioners, nurses, lab and diagnostics staff, therapists. They work in Frappe Desk workspaces: Healthcare, Outpatient, Inpatient, Diagnostics, Rehabilitation, Insurance, Practitioner, Reception, Hospital Administrator and Setup.
- **Administrators / billing**: configure Healthcare Settings, service units, medical departments, medical code standards and insurance payors and contracts. Billing goes through ERPNext Sales Invoice and Payment Entry.
- **Patients**: use the Vue **Patient Portal** at `/patient-portal` (role `Patient`). They can see appointments, book appointments, pay and view diagnostic reports.

## Feature areas

Patient management (including duplicate checking), outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, lab tests, observations and diagnostic reports, rehabilitation and physiotherapy (therapy plans and sessions, block-based therapy booking), medication and service requests, insurance (payor contracts, coverage, claims), and India ABDM regional integration. ERPNext covers pharmacy, purchasing, HR, accounts and assets.

The core domain doctypes are Patient, Healthcare Practitioner, Patient Appointment, Patient Encounter, Healthcare Service Unit, Lab Test, Clinical Procedure, Inpatient Record, Medical Department and Medical Code.
