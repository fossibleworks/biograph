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
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's unittest-based runner. Test classes subclass **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which extends ERPNext's `ERPNextTestSuite`. Recent commits migrated all fork tests to this base class.
- **Layout:** one `test_<doctype>.py` next to each doctype (`healthcare/healthcare/doctype/<name>/test_<name>.py`). About 80 exist. Shared fixtures live in `healthcare/tests/utils.py`: `BootStrapTestData` creates company, items, patients, practitioners, service units, templates, insurance payors, and so on. Test records use a `_Test ...` naming prefix.
- **Patterns:** call `super().setUp()` in `setUp`. Reuse factory helpers from other test modules (e.g. `create_appointment` from `test_patient_appointment`). Fetch fixtures deterministically (`frappe.get_list(..., pluck="name")`). Configure `Healthcare Settings` inside the test. Assert errors with `self.assertRaises(frappe.ValidationError)` or the specific subclass.
- **Running:** `bench --site <site> run-tests --app healthcare [--module ...]`. CI runs `run-parallel-tests` against MariaDB.
- **Coverage:** Codecov requires **85% patch coverage** on PRs to `develop`, and the project coverage may drop at most 0.5%. Coverage is captured on scheduled and non-PR runs.
- The PR labeler adds `needs-tests` when Python under `healthcare/` changes without any `test*.py` change.
- Known baseline: the fork has no CI history (see `wiki/upstream-sync-version-16.md`), so record pre-existing failures when you claim regressions.
