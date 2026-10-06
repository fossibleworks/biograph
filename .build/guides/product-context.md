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

**Biograph** (by Tacten / fossibleworks; shown as *fossibleHIS* in Build) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' *Marley Health*, with added features. It is a Frappe app named `healthcare` that adds a healthcare domain to **ERPNext**. `required_apps = ["frappe/erpnext"]` and the desk home is `/desk/healthcare`.

**Users:** healthcare practitioners, clinics, hospitals and their staff (front desk, nursing, lab, billing and insurance). Patients use the **Patient Portal**.

**Core feature areas** (README and the 139 doctypes under `healthcare/healthcare/doctype/`):
- Patient management, including patient duplicate checking (fork-specific, see `wiki/PATIENT-DUPLICATE*.md`)
- Outpatient and inpatient: Patient Appointment (with recurring and block-based therapy booking), Patient Encounter, inpatient records and medication orders
- Clinical procedures, rehabilitation and physiotherapy (Therapy Plan, Therapy Session, Exercise Type)
- Laboratory and diagnostics: Lab Test, Sample Collection, Observation, Diagnostic Report, Service Request
- Insurance: Insurance Payor, Payor Contract, Patient Insurance Policy and Coverage, claims
- Medical code standards and FHIR-style terminology. The design follows **HL7 FHIR**.
- Regional features: `healthcare/regional/india` and ABDM doctypes (`abdm_request`, `abdm_settings`)
- ERPNext integration for billing (Sales Invoice hooks), pharmacy and stock, HR and accounts

**Surfaces:**
- Frappe Desk UI (doctype forms, reports, dashboards, workspaces)
- A Vue 3 patient portal SPA served at `/patient-portal` (`healthcare/www/patient_portal.html`)
- Whitelisted API in `healthcare/healthcare/api/patient_portal.py`

**Upstream relationship:** `biograph-fh` is the fork's main branch. It is kept in sync with `earthians/marley` `version-16` by cherry-picking (`wiki/upstream-sync-version-16.md`). When they conflict, fork behaviour wins.
