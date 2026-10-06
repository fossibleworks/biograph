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
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`) against a real MariaDB site (`test_site`). There are no JS or Vue unit tests.
- **Layout:** each DocType keeps its test next to it, as `healthcare/healthcare/doctype/<name>/test_<name>.py` (about 85 test files). Shared fixtures live in `healthcare/tests/utils.py`.
- **Base class:** subclass `HealthcareTestSuite` from `healthcare.tests.utils`. It builds on ERPNext's `ERPNextTestSuite` and bootstraps master data through `BootStrapTestData` (`_Test Company`, patients, practitioners, service units, templates, insurance payors, …). Test records use the `_Test ` prefix.
- **Style:** `setUp` calls `super().setUp()` and often clears tables (`frappe.db.sql("delete from `tab…`")`). Module-level helpers such as `create_appointment(...)` build documents. Assertions use `self.assertEqual` and `self.assertRaises(frappe.ValidationError)` or a custom error subclass. Settings are toggled with `frappe.db.set_single_value("Healthcare Settings", …)`.
- **Coverage:** Codecov sets a **patch target of 85%** on PRs against `develop` and allows a 0.5% drop in project coverage. CI captures coverage only on non-PR (scheduled or push) runs.
- **Baseline caveat:** the fork `biograph-fh` has no CI test history. Record pre-existing failures before claiming a regression (see the wiki ledger).
