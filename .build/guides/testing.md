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
  - codecov.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's unittest-based runner. Test classes subclass `HealthcareTestSuite` (from `healthcare/tests/utils.py`), which extends `erpnext.tests.utils.ERPNextTestSuite`. `BootStrapTestData` there creates the shared master data: company, items, patients, practitioners, service units, templates and insurance payors. Record names start with `_Test ...`.
- **Layout:** each test sits next to its DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py`, with class `Test<DocType>`. There are about 85 test files.
- **Style:** `setUp` calls `super().setUp()`, often clears tables with `frappe.db.sql("delete from `tabX`")`, toggles settings with `frappe.db.set_single_value("Healthcare Settings", ...)`, and uses module-level factory helpers (`create_appointment`, `create_encounter`). Validation failures are checked with `self.assertRaises(frappe.ValidationError)` or a custom subclass.
- **Run:** `bench --site test_site run-parallel-tests --app healthcare`, which needs a full bench with ERPNext and MariaDB.
- **Coverage:** Codecov sets a **patch target of 85%** on PRs to `develop`, and project coverage may drop at most 0.5%. CI only captures coverage on non-PR (scheduled) runs.
- **Baseline caveat:** the `biograph-fh` fork has no CI run history (see `wiki/upstream-sync-version-16.md`). Record pre-existing failures there instead of treating them as regressions.
