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

## Framework

Tests are Frappe `unittest`-style integration tests that run against a real MariaDB site via `bench run-tests` / `run-parallel-tests`. There is no JS or portal test suite.

## Layout

- Each doctype has a `test_<doctype>.py` beside its controller (85 test files). Example: `healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py`.
- Test classes subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on ERPNext's `ERPNextTestSuite`. `BootStrapTestData` creates shared masters: company, items, patients, practitioners, service units, templates and so on.
- `setUp` calls `super().setUp()`, then clears the relevant tables (`frappe.db.sql("delete from `tabX`")`) and fetches fixtures with `frappe.get_list(..., pluck="name")[0]`.
- Tests build data with module-level helpers such as `create_appointment(...)`, and assert with `self.assertEqual`, `self.assertRaises` and similar.

## Expectations

- Codecov: **patch coverage target 85%** on PRs, and project coverage may drop at most 0.5%.
- The labeler adds `needs-tests` when `healthcare/**/*.py` changes without any `test*.py` change.
- CI skips PRs that only touch `.js`, `.css`, `.md`, `.html` or `.csv`.
- The fork has no CI baseline yet. Pre-existing failures on `biograph-fh` are tracked in the wiki sync ledger.
