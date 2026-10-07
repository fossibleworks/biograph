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
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

# Testing

## Framework
- Server tests use Frappe's test runner (unittest-style). Every test class extends **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which subclasses `ERPNextTestSuite`. Do not use `FrappeTestCase`, `IntegrationTestCase` or a bare `unittest.TestCase`. A recent commit migrated all fork tests to `HealthcareTestSuite`.
- `BootStrapTestData` in `healthcare/tests/utils.py` creates master data: company, items, patients, practitioners, service units, templates, and so on.

## Layout
- Tests sit next to the code: `healthcare/healthcare/doctype/<x>/test_<x>.py`. There are 85 test files.
- Factory helpers live in test modules (for example `create_appointment`, `create_encounter`, `create_therapy_plan`), and other tests import them across modules. Reuse these helpers instead of writing new fixtures.
- In `setUp`, always call `super().setUp()`. Look up records deterministically (`frappe.get_list(..., pluck="name")[0]`). Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.

## Running
- `bench --site test_site run-parallel-tests --app healthcare` in CI, on MariaDB 11.8.
- CI skips PRs that only touch `**.js/.css/.md/.html/.csv`. There are no JS or portal tests.

## Coverage expectations
- Coverage is collected on non-PR runs and uploaded to Codecov.
- `codecov.yml`: the **patch target is 85%** on PRs to develop, and the project may drop by at most 0.5%.
- The labeler adds a `needs-tests` label when `healthcare/**/*.py` changes without any `test*.py` change.
- The fork has no CI baseline for `biograph-fh` (see the wiki ledger), so record any pre-existing failures when you report results.
