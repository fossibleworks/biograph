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

- **Framework:** Frappe's test runner (unittest-based), run with `bench run-tests` or `run-parallel-tests` against a real MariaDB site. There are no JS or portal unit tests.
- **Layout:** tests sit next to the code as `doctype/<name>/test_<name>.py` (about 85 files). Shared fixtures are in `healthcare/tests/utils.py`.
- **Base class:** every test class subclasses `HealthcareTestSuite` (from `healthcare.tests.utils`, which extends `ERPNextTestSuite`). `BootStrapTestData` seeds the master data: company, items, patients, practitioners, service units, templates and insurance payors. Test records use the `_Test ...` naming prefix.
- **Patterns:** call `super().setUp()`. Reuse helper factories from other test modules (for example `create_appointment` from `test_patient_appointment`). Set Healthcare Settings explicitly inside the test. Use `self.assertRaises(frappe.ValidationError)` or a specific error subclass for validation paths.
- **Coverage:** Codecov requires **85% patch coverage** on PRs to `develop`, and the project coverage may not drop more than 0.5%. Coverage is captured only on non-PR (scheduled) runs.
- **Baseline caveat:** the fork (`biograph-fh`) has no historical CI run. The first CI run on a goal PR is the baseline. No local bench may be available, so record that clearly rather than claiming tests passed.
