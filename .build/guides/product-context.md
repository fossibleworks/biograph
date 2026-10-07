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
  - patient_portal/src/PatientPortal.vue
---

**Biograph** (fossibleHIS, by Tacten) is an open-source hospital information system (HIS). It is a fork of earthians' Marley Health with added features. It ships as the Frappe app `healthcare` (app_title "Biograph"), adds the healthcare domain to ERPNext, and models most of its data on HL7 FHIR.

**Users:** healthcare practitioners, clinics and hospitals (desk users such as practitioners, nurses, lab and billing staff), plus patients through the Vue patient portal (`/patient-portal`).

**Main feature areas:**
- Patient management and duplicate checking
- Outpatient appointments, including block-based therapy booking
- Inpatient records, medication orders and entries
- Clinical procedures
- Rehabilitation and physiotherapy (therapy plans and sessions)
- Laboratory (Lab Test, Observation, Diagnostic Report, sample collection)
- Medication and medication requests
- Insurance (payor, contract, claim, coverage, eligibility)
- Code systems and FHIR terminology
- Fee validity and healthcare packages
- India ABDM integration (`healthcare/regional/india`)

Facilities are mapped as Healthcare Service Units and specialities as Medical Departments. ERPNext provides billing (Sales Invoice, Payment Entry), pharmacy stock, HR and accounts.

**Deployment:** install with `bench get-app` and `bench --site <site> install-app healthcare`. It is also offered on Frappe Cloud.
