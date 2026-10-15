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
  - patient_portal/src/components/BookAppointmentModel.vue
  - wiki/insurance-parity-report.md
---

**Biograph** (app name `healthcare`, app title "Biograph") is an open-source Hospital Information System (HIS). It is a fork of Marley Health (earthians) with added features, and Tacten / FossibleWorks maintains it as "fossibleHIS". It is a **Frappe app that requires ERPNext** (`required_apps = ["frappe/erpnext"]`), and its home is the Frappe Desk at `/desk/healthcare`.

**Users:** clinics, hospitals and individual practitioners. Inside the Desk that means front desk staff, doctors (Healthcare Practitioner), nurses and lab staff. Patients use a separate **Patient Portal** at `/patient-portal`, which needs the `Patient` role.

**Main features** (README and doctype list): patient management, outpatient and inpatient care (Patient Appointment, Patient Encounter, Inpatient Record), clinical procedures, rehab and physiotherapy (Therapy, Exercise), laboratory work (Lab Test, Sample Collection, Observation, Diagnostic Report), medication and medication requests, nursing tasks, insurance (Payor, Contract, Coverage, Claim), fee validity and billing through ERPNext Sales Invoice and Payment Entry, and medical coding (Code System, Code Value, Code Value Set; most of the design follows HL7 FHIR). A regional India ABDM integration lives in `healthcare/regional/india/abdm`.

ERPNext supplies pharmacy, stock, purchasing, HR, accounts and assets. In the portal, patients view appointments, orders and lab results, book appointments by department and practitioner, and pay bills.
