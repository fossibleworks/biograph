---
title: Testing
category: testing
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
  - healthcare/tests/utils.py
  - healthcare/hooks.py
  - .github/workflows/ci.yml
  - codecov.yml
---

- **Framework:** Frappe's test runner over `unittest`. New tests subclass **`frappe.tests.IntegrationTestCase`** (about 69 files). Older ones use `FrappeTestCase` and a few use plain `unittest`.
- **Layout:** each DocType folder has `test_<doctype>.py` next to the controller. Shared helpers are in `healthcare/tests/utils.py` and `healthcare/tests/test_utils.py`. `before_tests = healthcare.healthcare.utils.before_tests` in hooks sets up fixtures (company, etc.).
- **Fixtures:** tests build data with factory helpers that other tests import (e.g. `create_healthcare_docs`, `create_appointment`, `create_healthcare_service_items` from `test_patient_appointment`). They declare `EXTRA_TEST_RECORD_DEPENDENCIES = ["Company"]`. They often clear tables in `setUp` and change `Healthcare Settings` directly.
- **Running:** `bench --site test_site run-parallel-tests --app healthcare` in CI against MariaDB with ERPNext and payments installed. Server tests run on PRs (except PRs touching only css/js/md/html/csv) and nightly.
- **Coverage:** captured on non-PR runs and uploaded to Codecov. **Patch coverage target 85%** on PRs to develop. Project coverage may not drop more than 0.5%.
- There are no JS/Vue unit tests. UI behaviour is verified manually (the PR template asks for screenshots/GIFs).
