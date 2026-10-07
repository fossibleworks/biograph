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
  - codecov.yml
  - .github/helper/install.sh
---

- **Framework:** Frappe's test runner (`bench run-tests --app healthcare`) on top of ERPNext's test utilities. Tests need a real site with MariaDB, so `.github/helper/install.sh` builds a bench with frappe, payments, erpnext and healthcare (`version-16` for fork branches).
- **Layout:** each doctype's tests live next to it as `doctype/<name>/test_<name>.py` (85 test files). Shared helpers are in `healthcare/tests/`.
- **Base class:** every test class subclasses `HealthcareTestSuite` (`from healthcare.tests.utils import HealthcareTestSuite`), which extends `erpnext.tests.utils.ERPNextTestSuite`. `BootStrapTestData` in `healthcare/tests/utils.py` creates the shared master data: company, service items, practitioners, patients, service units, templates and insurance payors. Test records use the `_Test ...` naming prefix.
- **Errors:** assert custom exceptions with `assertRaises(<Domain>Error)`, e.g. `OverlapError` or `MaximumCapacityError`.
- **Coverage:** Codecov requires **85% patch coverage** on PRs (threshold 0%), and project coverage may not drop by more than 0.5%.
- **CI caveat:** the fork has no server-test workflow (`ci.yml`) in `.github/workflows`, so there is no CI baseline (see the upstream sync ledger). Run tests locally and report the results.
