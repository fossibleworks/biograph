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
  - healthcare/healthcare/doctype/nursing_task/test_nursing_task.py
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's test runner (unittest-based), run through `bench run-tests` / `run-parallel-tests` against a real MariaDB site with ERPNext and payments installed.
- **Layout:** tests sit next to the code as `test_<doctype>.py` inside each doctype folder (85 test files). There are also report tests (`report/*/test_*.py`), `healthcare/regional/india/abdm/test_abdm.py`, and `healthcare/tests/test_utils.py`.
- **Base class:** subclass `healthcare.tests.utils.HealthcareTestSuite`, which builds on `erpnext.tests.utils.ERPNextTestSuite`. `BootStrapTestData` creates shared master data: `_Test Company`, patients, practitioners, service units, templates, insurance payors and so on. Call `super().setUp()` and reuse factory helpers from other test modules, e.g. `create_appointment` from `test_patient_appointment`, instead of creating new fixtures.
- **Assertions:** `assertEqual` / `assertTrue` on `frappe.db.get_value` results. Use `self.assertRaises(frappe.ValidationError, doc.save)` for validation paths. Tests often turn on `Healthcare Settings` flags with `save(ignore_permissions=True)`.
- **Coverage expectations (codecov.yml):**
  - project status target is `auto`, with a 0.5% threshold
  - patch coverage target is **85%** on PRs to `develop`
  - coverage is only captured on non-PR (scheduled) CI runs
- **Labeler:** a PR that changes `healthcare/**/*.py` without touching any `test*.py` gets the `needs-tests` label.
- CI skips server tests for PRs that change only `.js`, `.css`, `.md`, `.html` or `.csv` files. Front-end changes have no automated tests.
- **Fork caveat:** according to `wiki/upstream-sync-version-16.md`, `ci.yml` has never run on `fossibleworks/biograph`, so there is no CI failure baseline. Record local test results when you change behaviour.
