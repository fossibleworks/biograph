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
  - healthcare/tests/test_utils.py
  - codecov.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe/ERPNext integration tests, which are unittest-style and run against a real MariaDB site. The shared base class is `healthcare.tests.utils.HealthcareTestSuite`, which extends `erpnext.tests.utils.ERPNextTestSuite`. `BootStrapTestData` creates the master data: company, items, departments, patients, practitioners, service units, templates and insurance payors. Records are prefixed `_Test ...`.
- **Layout:** `test_<doctype>.py` sits next to its DocType, in `healthcare/healthcare/doctype/<name>/`, and there are about 110 of these files. Shared tests live in `healthcare/tests/`. Tests subclass `HealthcareTestSuite`, call `super().setUp()`, and often clear tables with `frappe.db.sql("delete from `tab...`")`. Module-level `create_*` helpers build fixtures.
- New tests must use `HealthcareTestSuite`. Recent work moved all fork tests onto it.
- **Running:** CI uses `bench --site test_site run-parallel-tests --app healthcare`.
- **Coverage:** Codecov expects **85% patch coverage** on PRs to `develop`, and the project coverage threshold allows a 0.5% drop. Coverage is collected only on non-PR (scheduled) runs.
- **Frontend:** there are no JS or Vue unit tests.
- **Fork note:** `biograph-fh` has no CI baseline, so record known baseline failures in the wiki ledger.
