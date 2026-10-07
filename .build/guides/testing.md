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
  - healthcare/healthcare/doctype/practitioner_availability/test_practitioner_availability.py
  - .github/workflows/ci.yml
  - codecov.yml
---

**Framework:** the Frappe/ERPNext test runner, which is based on unittest. Tests run against a real MariaDB site through bench:
```sh
bench --site test_site run-parallel-tests --app healthcare
```
You cannot run tests without a bench site.

**Layout**
- Each DocType has `test_<doctype>.py` next to its controller, for example `healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py`. There are about 85 test files.
- Shared fixtures are in `healthcare/tests/utils.py`:
  - **`HealthcareTestSuite`** extends ERPNext's `ERPNextTestSuite`.
  - `BootStrapTestData` creates master data: `_Test Company`, patients, practitioners, service units, templates, insurance payors and more.
- Test classes are named `Test<DocType>(HealthcareTestSuite)` and call `super().setUp()`.
- Test records use the `_Test ...` naming prefix.
- Module-level `create_<thing>()` helpers build documents, for example `create_appointment`, which other tests import.
- Use `frappe.db.set_single_value("Healthcare Settings", ...)` to toggle settings per test.
- Use `self.assertRaises(frappe.ValidationError)` or a custom ValidationError subclass for negative cases.

**All fork tests have been migrated to `HealthcareTestSuite`.** New tests must subclass it, not `FrappeTestCase` or `unittest.TestCase` directly.

**Coverage**
- Codecov **patch target is 85%** (threshold 0%) on PRs.
- The project status uses `auto` with a 0.5% threshold.
- Coverage is captured only on non-PR (scheduled) runs and uploaded to Codecov.

**CI notes:** the fork has no historical CI baseline. Compare any test failure against the commit that introduced it, using the sync ledger.
