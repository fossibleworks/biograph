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
  - healthcare/healthcare/doctype/allergy/test_allergy.py
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's test runner (unittest based), run through bench: `bench --site test_site run-parallel-tests --app healthcare`. CI runs the tests against a fresh `test_site` on MariaDB.
- **Base class:** every test class extends `HealthcareTestSuite` from `healthcare/tests/utils.py` (82 classes). That class extends ERPNext's `ERPNextTestSuite`. Shared master data (`_Test Company`, patients, practitioners, service units, templates, insurance payors…) is built by `BootStrapTestData`. Reuse or extend it instead of creating ad-hoc fixtures. Recent commits migrated all fork tests to this base.
- **Layout:** `test_<doctype>.py` lives next to its controller in `doctype/<name>/` (85 test files). Cross-cutting helpers go in `healthcare/tests/`.
- **Determinism:** many recent `fix(tests)` commits make tests deterministic (fixed dates, explicit customer groups, a `super().setUp()` call). Follow the same rules.
- **Coverage:** Codecov expects **85% patch coverage** on PRs to `develop` and allows a 0.5% project drop. Coverage is collected on non-PR runs.
- The PR labeler adds `needs-tests` when Python under `healthcare/` changes without any `test*.py` change.
