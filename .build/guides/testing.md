---
title: Testing
category: testing
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - .github/workflows/ci.yml
  - codecov.yml
  - healthcare/tests/utils.py
  - healthcare/tests/test_utils.py
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/healthcare/doctype/insurance_claim/test_insurance_claim.py
  - healthcare/hooks.py
---

## Framework
- Server tests run on Frappe's test runner via **bench** (`bench --site test_site run-parallel-tests --app healthcare` in CI) against a real MariaDB site with ERPNext and payments installed.
- Base classes: most tests use `frappe.tests.IntegrationTestCase` (~67 classes). Some legacy tests use `FrappeTestCase` (7). Newer insurance tests use **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which builds on ERPNext's `ERPNextTestSuite` with `BootStrapTestData` master data such as `_Test Insurance Payor`.
- `hooks.py` sets `before_tests = healthcare.healthcare.utils.before_tests`.

## Layout
- Put tests next to the code: `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 test files), with classes named `Test<DocType>`.
- Shared helpers go in `healthcare/tests/test_utils.py` (e.g. `create_encounter`) and `healthcare/tests/utils.py`. Add new reusable fixtures there; the existing TODO says to move helpers there.
- Test records use the `_Test ...` naming prefix. Tests often clean tables in `setUp`.

## Coverage
- Codecov **patch target 85%** on PRs (threshold 0%). The project status is `auto` with a 0.5% threshold.
- Coverage is only captured on scheduled and non-PR runs.
- CI skips server tests for PRs touching only `.js/.css/.md/.html/.csv`.

## Expectations
Add or extend `test_<doctype>.py` for any server-side behaviour change. Prefer `IntegrationTestCase` or `HealthcareTestSuite` for new tests.
