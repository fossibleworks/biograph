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
---

**Biograph** (by Tacten / FossibleWorks; internally the fossibleHIS fork `fossibleworks/biograph`) is an open-source **Hospital Information System (HIS)**. It is a fork of earthians' **Marley Health** with extra features. It ships as the Frappe app `healthcare` and adds the healthcare domain to **ERPNext**.

**Who uses it:** clinics, hospitals and healthcare practitioners use it as staff in the Frappe desk. Patients use it through a Vue **Patient Portal** at `/patient-portal`, where they book appointments, view appointments and diagnostic reports, and pay.

**Main features (from the README):** patient management, outpatient and inpatient care, clinical procedures, rehabilitation and physiotherapy (therapy plans and sessions), laboratory and diagnostics (observations, sample collection, diagnostic reports), medication requests, insurance (payors and contracts), fee validity, and healthcare packages. It can be configured with multiple medical code standards (code systems and values). Facilities are modelled as **Healthcare Service Units** and specialities as **Medical Departments**. Much of the data model follows **HL7 FHIR**. Indian **ABDM** integration lives in `healthcare/regional/india`.

ERPNext supplies pharmacy and stock, purchasing, HR, accounting and invoicing (Sales Invoice, Payment Entry), and assets.

**Fork features documented in `wiki/`:** block-based therapy appointment booking, the patient duplicate checker, FHIR terminology-service parity, and insurance parity. The fork regularly syncs commits from upstream `earthians/marley` `version-16` (see `wiki/upstream-sync-version-16.md`). When there is a conflict, fork behaviour wins.
