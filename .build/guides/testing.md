---
title: Testing
category: testing
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/tests/utils.py
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
  - codecov.yml
  - .github/helper/install.sh
---

- **Framework:** Frappe's unittest-based test runner, executed inside a bench site (`bench --site test_site run-tests --app healthcare`). The CI bench is built by `.github/helper/install.sh`, which uses Frappe and ERPNext `version-16` for fork branches such as `biograph-fh` and `goal/*`.
- **Layout:** tests live next to their DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 files). Shared fixtures and helpers are in `healthcare/tests/utils.py` and `healthcare/tests/test_utils.py`.
- **Base class:** test classes are named `Test<DocType>` and subclass **`HealthcareTestSuite`** from `healthcare.tests.utils`. `setUp` must call `super().setUp()`.
- **Fixtures:** reuse the `create_*` helpers exported by sibling tests, for example `create_appointment` from `test_patient_appointment` or ERPNext's `make_pos_profile`. Tests often clear tables in `setUp` and toggle `Healthcare Settings` values.
- **Coverage:** Codecov requires **85% patch coverage** on pull requests, and project coverage may drop by at most 0.5%.
- **Baseline caveat:** the fork has no CI test history yet, so the first CI run on a goal PR becomes the baseline. Lint baselines are recorded per batch in the wiki ledger.
