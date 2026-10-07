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
---

# Biograph (fossibleHIS)

Biograph is an open-source **hospital information system (HIS)** by Tacten. It forks and extends *Marley Health* (earthians/marley). It ships as a Frappe app named `healthcare` that adds a health domain to **ERPNext**, and much of its data model follows **HL7 FHIR**.

## Who uses it
- Healthcare practitioners, clinics and hospitals: front desk, doctors, nurses, lab staff and billing/insurance staff. They work in the Frappe Desk UI.
- Patients use the **Patient Portal** (Vue SPA at `/patient-portal`) to book appointments, view prescriptions and diagnostic results, and pay bills.

## Main feature areas
- Patient management and duplicate-patient checking
- Outpatient (Patient Appointment, Patient Encounter, Fee Validity) and Inpatient (Inpatient Record, service-unit occupancy)
- Clinical Procedures, Therapy/Rehabilitation (Therapy Plan, Exercise), block-based therapy booking
- Laboratory and diagnostics (Lab Test, Sample Collection, Observation, Diagnostic Report)
- Medication Requests and Service Requests
- Insurance (Payor, Contract, Patient Insurance Policy/Coverage, claims)
- Medical code standards (Code System, Code Value), FHIR terminology, ABDM (India) integration
- Facilities are modelled as **Healthcare Service Units**; specialities are **Medical Departments**.

ERPNext provides pharmacy and stock, purchasing, HR, accounts and assets. Healthcare billing is done through Sales Invoice and Payment Entry overrides.

Install with `bench get-app` and `bench --site <site> install-app healthcare`. Documentation lives on DeepWiki and in `wiki/`.
