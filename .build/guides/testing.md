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

**Framework:** Frappe/ERPNext unittest-based tests, run with `bench run-tests` / `run-parallel-tests` against a real MariaDB site that also has erpnext and payments installed.

**Layout**
- Each doctype keeps its tests next to it: `healthcare/healthcare/doctype/<name>/test_<name>.py`.
- Shared fixtures live in `healthcare/tests/utils.py`. `BootStrapTestData` creates master data (`_Test Company`, practitioners, patients, service units, templates, insurance payors, ...) through `make_records`, and `HealthcareTestSuite(ERPNextTestSuite)` is the base class.

**Conventions**
- Test classes subclass `HealthcareTestSuite`. The fork recently migrated all of its tests to this base class, so don't use `FrappeTestCase` or `unittest.TestCase` directly.
- Always call `super().setUp()`.
- Clean up with `frappe.db.sql("delete from `tabX`")` in `setUp` when needed.
- Make data deterministic: look records up with `frappe.get_list(..., pluck="name")`, set settings explicitly with `frappe.db.set_single_value("Healthcare Settings", ...)`, and set the customer group explicitly.
- Test record names use the `_Test ...` prefix.
- Module-level helper factories such as `create_appointment(...)` and `create_encounter(...)` sit in the test module and are imported by other tests.

**Coverage expectations**
- Codecov patch target is **85%** on PRs to develop; the project threshold is 0.5%.
- The PR labeler adds `needs-tests` when `healthcare/**/*.py` changes without any `test*.py` change.
- CI collects coverage only on scheduled and non-PR runs.

**Fork caveat:** `wiki/upstream-sync-version-16.md` notes there is no CI baseline on `biograph-fh`. The first CI run on a goal PR becomes the baseline.
