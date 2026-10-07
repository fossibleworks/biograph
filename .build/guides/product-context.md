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
  - healthcare/www/patient_portal.py
---

**Biograph (by Tacten / FossibleWorks)** is an open-source Hospital Information System (HIS). It is a fork of earthians' Marley Health with further changes. It ships as the Frappe app `healthcare` and adds the health domain to ERPNext.

**Who uses it:** clinics, hospitals and healthcare practitioners. Patients also use it through a self-service **Patient Portal** at `/patient-portal`, a Vue SPA where they book appointments, view orders and diagnostics, and pay bills.

**Core capabilities** (README and the 139 doctypes under `healthcare/healthcare/doctype`):
- Patient management, patient duplicate checking, patient history and medical records
- Outpatient/Inpatient management: Patient Appointment (recurring, block-based therapy booking, practitioner unavailability), Inpatient Record, service units
- Clinical Procedures, Rehabilitation/Physiotherapy (therapy plans and sessions), Nursing tasks
- Laboratory: lab tests, sample collection, observations, diagnostic reports
- Medication requests, Service Requests (orders), Treatment plans
- Insurance: payors, contracts, policies, coverage, claims
- Medical coding: Code System / Code Value, following HL7 FHIR concepts (terminology-service parity is planned)
- Regional: India ABDM integration (`healthcare/regional/india`)
- Billing goes through ERPNext Sales Invoice and Payment Entry hooks

Pharmacy, purchasing, HR, accounts and assets come from ERPNext itself. Domain vocabulary such as "Healthcare Practitioner", "Service Unit", "Medical Department" and "Fee Validity" comes from the doctype names, and new work should reuse those names.

The working branch here is `biograph-fh` (the fossibleHIS fork, `fossibleworks/biograph`). It is periodically synced with upstream `earthians/marley` `version-16` (see `wiki/upstream-sync-version-16.md`).
