---
title: Testing
category: testing
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/tests/utils.py
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
  - healthcare/healthcare/doctype/practitioner_availability/test_practitioner_availability.py
  - .github/workflows/ci.yml
  - codecov.yml
---

# Testing

## Framework
- Frappe/ERPNext server tests (unittest style), run with `bench --site test_site run-parallel-tests --app healthcare` (CI) or `bench run-tests`.
- All test classes extend **`HealthcareTestSuite`** (`healthcare/tests/utils.py`), which subclasses ERPNext's `ERPNextTestSuite`. `BootStrapTestData` builds the shared master data: company, items, patients, practitioners, service units, templates and insurance payors. Test records use `_Test ...` names.
- There are no JS or portal unit tests.

## Layout
- Tests sit next to their doctype: `healthcare/healthcare/doctype/<name>/test_<name>.py`, class `Test<DocTypeName>(HealthcareTestSuite)`.
- Reuse factory helpers from other doctypes' tests instead of duplicating them (for example, `from ...patient_appointment.test_patient_appointment import create_appointment`).
- Call `super().setUp()` in `setUp`. Tests often reset tables with `frappe.db.sql("delete from `tab...`")` and toggle `Healthcare Settings` flags.
- Assert validation failures with `self.assertRaises(frappe.ValidationError)` or with a specific subclass.

## Coverage expectations
- Codecov: **patch coverage target 85%** on PRs to `develop`. Project coverage may drop by at most 0.5%.
- Coverage is captured on scheduled (non-PR) CI runs.
- On the fork there is no CI baseline yet. The first CI run on a goal PR becomes the baseline (see the sync ledger).
