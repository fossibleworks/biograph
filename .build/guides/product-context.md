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

Biograph (this fork's Build name is **fossibleHIS**, repo `fossibleworks/biograph`) is an open-source **Hospital Information System (HIS)**. Tacten maintains it as a fork of earthians' **Marley Health** and adds its own features. It is a Frappe app named `healthcare` that adds the health domain to **ERPNext**. Much of the data model follows **HL7 FHIR**.

**Who uses it:** healthcare practitioners, clinics and hospitals (desk users), plus patients through a Patient Portal.

**Main feature areas, each built as Frappe DocTypes under `healthcare/healthcare/doctype/`:**
- Patients and patient duplicate check
- Outpatient work: Patient Appointment, Patient Encounter, Fee Validity, practitioner schedules and unavailability, block-based therapy booking
- Inpatient work: Inpatient Record, medication orders and entries, nursing tasks, discharge summary
- Clinical Procedures, Rehabilitation and Physiotherapy (Therapy Plan, Exercise), Laboratory (Lab Test, Sample Collection, Observation, Diagnostic Report)
- Medical code standards (Code System, Code Value) and FHIR terminology
- Insurance: Payor, Contract, Eligibility Plan, Claim
- Billing through ERPNext Sales Invoice and Payment Entry overrides
- Regional support for India (ABDM)

ERPNext provides pharmacy and supplies, purchasing, HR, accounts, assets and quality. The app installs into an ERPNext bench with `bench get-app` and `bench --site <site> install-app healthcare`.

**Fork relationship:** the default branch `biograph-fh` is synced from upstream `earthians/marley` `version-16` in batches. `wiki/upstream-sync-version-16.md` is the sync ledger. When a fork change conflicts with upstream, the fork's behaviour wins.
