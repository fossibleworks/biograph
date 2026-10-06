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
  - patient_portal/src/PatientPortal.vue
---

**Biograph** (by Tacten, maintained by fossibleworks in the `fossibleworks/biograph` repo, where it is branded fossibleHIS) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' *Marley Health* with added features. It ships as a Frappe app named `healthcare` (`app_title = "Biograph"`). It adds the health domain to ERPNext and is installed on a bench next to ERPNext (`required_apps = ["frappe/erpnext"]`).

**Users:** healthcare practitioners, clinics and hospitals (clinical staff, nurses, lab staff, front desk and billing). Patients use a separate Vue **Patient Portal** to see appointments and diagnostics and to book and pay.

**Feature areas** (from the README and doctypes): patient management, outpatient and inpatient management (Inpatient Record, Inpatient Medication Order and Entry), patient appointments (including block-based and therapy booking and practitioner availability), clinical procedures, rehabilitation and physiotherapy (Therapy Plan, Exercise), lab management (Lab Test, Observation, Diagnostic Report), medication and medication requests, nursing tasks, insurance (Payor, Contract, Eligibility, Claim), patient duplicate detection, and medical code standards (Code System and Code Value, modelled on HL7 FHIR). Pharmacy, purchasing, HR, accounts and assets come from ERPNext. Billing goes through ERPNext Sales Invoice hooks.

There are India-specific regional features (ABDM) under `healthcare/regional/india` and the ABDM doctypes. The desk home is `/desk/healthcare`. The patient portal is served from `healthcare/www/patient_portal`.
