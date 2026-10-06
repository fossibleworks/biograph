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
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

## Framework
- Tests use Frappe/ERPNext integration tests run by bench (`run-parallel-tests` in CI) against a real MariaDB site (`test_site`).
- Test classes extend **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which subclasses `ERPNextTestSuite`. Recent commits moved all tests off `IntegrationTestCase` and `EXTRA_TEST_RECORD_DEPENDENCIES`.
- Master data comes from **`BootStrapTestData`** (`healthcare/tests/utils.py`). It creates `_Test Company`, service items, patients, practitioners, service units, templates, insurance payors and other masters. Tests **reuse these records** (e.g. `frappe.get_list("Patient", pluck="name")[0]`) and do not create their own. Do not delete master data after tests.
- Always call `super().setUp()` in `setUp`. Keep tests deterministic; several recent fixes targeted ordering and date flakiness.
- Reuse helper factories exported from other tests (e.g. `create_appointment` in `test_patient_appointment.py`).

## Layout
`healthcare/healthcare/doctype/<doctype>/test_<doctype>.py`, next to the controller (85 test files). Report tests live in the report folder.

## Coverage expectations
- Codecov patch target is **85%** on PRs to `develop`. Project coverage may drop by at most 0.5%.
- Coverage is captured on scheduled and non-PR runs.
- The labeler adds **`needs-tests`** when a PR changes `healthcare/**/*.py` without changing any `test*.py`.

## Fork note
The fork's CI has no history on `biograph-fh`, so the first CI run on a goal PR serves as the baseline. Compare failures against the commit that introduced them.
