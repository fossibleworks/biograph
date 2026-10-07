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
  - wiki/DESIGN-BLOCKBASED-THERAPY-APPOINTMENT-BOOKING.md
---

**Biograph by Tacten** (Build calls it *fossibleHIS*) is an open-source **hospital information system (HIS)**. It is a fork of **earthians Marley Health** with extra features added. It ships as a Frappe app named `healthcare` (app title "Biograph") and needs **ERPNext** installed (`required_apps = ["frappe/erpnext"]`).

**Who uses it:** hospitals, clinics and healthcare practitioners. Patients also use it through a self-service **Patient Portal**.

**Main features** (from the README and the doctype tree):
- Patient management, Patient Appointments (including recurring and block-based therapy booking), Fee Validity
- Outpatient work (Patient Encounter) and inpatient work (Inpatient Record, Inpatient Medication Orders and Entries)
- Clinical Procedures, Rehabilitation and Physiotherapy (Therapy Plans and Sessions, Exercise Types)
- Laboratory: Lab Tests, Observations, Diagnostic Reports, Sample Collection
- Medical code standards (Code System, Code Value, Code Value Set). Most of the design follows **HL7 FHIR**.
- Insurance: Payor, Payor Contract, Patient Insurance Policy and Coverage, claims
- India regional (ABDM) integration under `healthcare/regional/india` and the ABDM doctypes
- Facilities are modelled as **Healthcare Service Units** and specialities as **Medical Departments**
- Pharmacy, purchasing, HR, accounts and assets are handled by ERPNext. Billing goes through Sales Invoice hooks.

**Entry points:**
- Desk app home: `/desk/healthcare`.
- Patient Portal: a Vue SPA served from `healthcare/www/patient_portal.html`. It covers booking appointments, choosing a department or practitioner, payment and diagnostics.
- After login, users land on a home page set by their role (`on_login` hook).

Feature design notes live in `wiki/`, for example patient duplicate checking and block-based therapy appointment booking.
