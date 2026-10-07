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
---

**Biograph** (by Tacten; deployed under the name *fossibleHIS*) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians **Marley Health**, with additional features. It ships as a Frappe app named `healthcare`, depends on ERPNext (`required_apps = ['frappe/erpnext']`), and much of its data model follows **HL7 FHIR**.

**Users:** healthcare practitioners, clinics, hospitals, and lab, nursing and billing staff, all working in the Frappe desk. Patients use a separate Vue **Patient Portal** (`/patient-portal`) to view and book appointments, see diagnostics and make payments.

**Main feature areas:** patient management, outpatient appointments and encounters, inpatient records and medication, clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions, block-based therapy booking), laboratory (lab tests, observations, diagnostic reports), medical code standards, service units and medical departments, insurance (payors, contracts, policies, coverage), patient duplicate detection, and India ABDM regional integration. ERPNext covers pharmacy, purchasing, HR, accounts and assets.

The app title in `hooks.py` is `Biograph` and the desk home is `/desk/healthcare`.
