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
  - codecov.yml
  - .github/workflows/ci.yml
---

**Framework**
- Frappe/ERPNext integration tests, run with `bench run-tests` / `run-parallel-tests` against a real MariaDB site.
- No JS or Vue unit-test setup exists in the repo.

**Layout**
- One `test_<doctype>.py` inside each DocType folder (about 80 files), for example `doctype/fee_validity/test_fee_validity.py`.
- Also `healthcare/custom_doctype/test_sales_invoice.py` and `healthcare/tests/test_utils.py`.

**Base class**
- Tests subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`, which extends ERPNext's `ERPNextTestSuite`.
- Fork tests were recently migrated onto it. Do not use `FrappeTestCase` or a raw `unittest.TestCase`.
- `BootStrapTestData` in `healthcare/tests/utils.py` creates master data: company, service items, patients, practitioners, service units, templates and insurance payors. Test records are named with a `_Test ...` prefix.

**Writing tests**
- Reuse creators exported by other test modules (`create_appointment`, `update_status` from `test_patient_appointment`, `make_pos_profile` from ERPNext) instead of duplicating fixtures.
- Configure behaviour through the `Healthcare Settings` single doc inside the test.
- Make data deterministic. Recent fixes addressed non-deterministic patient initialisation.

**Coverage**
- `codecov.yml` sets a patch target of **85%**. The project status uses an auto target with a 0.5% threshold.
- Coverage is captured only on scheduled (non-PR) CI runs.
- CI skips server tests for PRs that change only `.js`, `.css`, `.md`, `.html` or `.csv` files.

**Baseline**
- `ci.yml` has never run on the fork branch `biograph-fh` (see `wiki/upstream-sync-version-16.md`). The first CI run on a goal PR serves as the baseline.
