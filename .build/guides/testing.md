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

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`) against a real MariaDB site with ERPNext installed.
- **Base class:** `healthcare.tests.utils.HealthcareTestSuite`, which subclasses `erpnext.tests.utils.ERPNextTestSuite`. `BootStrapTestData` in `healthcare/tests/utils.py` seeds master data: company, items, departments, patients, practitioners, service units, templates.
- **Layout:** tests sit next to the code as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 files). Shared helpers live in `healthcare/tests/`.
- **Style:**
  - Test classes are `class Test<Doctype>(HealthcareTestSuite)`, with `setUp` calling `super().setUp()`.
  - Some `setUp` methods clear tables with `frappe.db.sql("delete from `tab…`")`.
  - Tests define module-level factories such as `create_appointment(...)`.
  - Change settings with `frappe.db.set_single_value("Healthcare Settings", ...)` and assert with `self.assertEqual` / `assertRaises`.
- **Coverage:**
  - Codecov wants **85% patch coverage** on PRs and lets project coverage drop at most 0.5%.
  - CI captures coverage only on non-PR (scheduled) runs.
  - The PR labeler adds a **`needs-tests`** label when `healthcare/**/*.py` changes without any `test*.py` change.
- **Fork baseline:** the fork has no CI history yet (see `wiki/upstream-sync-version-16.md`). The first goal-PR CI run is the baseline, and each failure must be traced to the commit that introduced it.
