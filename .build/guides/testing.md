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
  - codecov.yml
  - .github/workflows/ci.yml
---

# Testing

## Framework
- Tests are Frappe/ERPNext integration tests run with `bench run-tests` / `run-parallel-tests`, against a real MariaDB site.
- Every test class extends **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which subclasses ERPNext's `ERPNextTestSuite`. Recent work moved all fork tests onto it, and no test uses `FrappeTestCase` or `IntegrationTestCase` directly.
- `healthcare/tests/utils.py` also holds `BootStrapTestData`, which builds the shared master data: `_Test Company`, service and stock items, practitioners, patients, service units, templates, insurance payors, and so on. Records use the `_Test ...` naming.

## Layout
- Each doctype's test sits beside it: `healthcare/healthcare/doctype/<name>/test_<name>.py`. There are about 85 such files.
- Tests reuse factory helpers exported from other test modules, for example `from ...patient_appointment.test_patient_appointment import create_appointment`.

## Conventions
- Always call `super().setUp()` in `setUp`.
- Look up fixtures deterministically, for example `frappe.get_list("Patient", pluck="name")`, and do not create ad-hoc companies.
- Change settings through `frappe.get_single("Healthcare Settings")` followed by `.save(ignore_permissions=True)`.
- Name test methods `test_<behaviour>`.

## Coverage
- Codecov is set up with patch coverage **target 85%** on PRs and a project threshold of 0.5%.
- CI collects coverage only on scheduled and non-PR runs (`WITH_COVERAGE`/`CAPTURE_COVERAGE`).
- Bug fixes and features should add or update the `test_<doctype>.py` next to the code they change.
