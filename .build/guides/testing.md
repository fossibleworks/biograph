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
  - .github/workflows/ci.yml
  - codecov.yml
  - .github/labeler.yml
---

- **Framework:** Frappe's unittest-based test runner, run inside a bench site (`bench --site test_site run-parallel-tests --app healthcare`). There is no pytest and no JS or UI test suite.
- **Layout:** tests sit next to the code as `test_<doctype>.py` in each doctype folder (about 85 files), for example `healthcare/healthcare/custom_doctype/test_sales_invoice.py`. Shared fixtures live in `healthcare/tests/utils.py`, and `healthcare/tests/test_utils.py` exists alongside it.
- **Base class:** subclass `HealthcareTestSuite` from `healthcare.tests.utils`. It builds on `erpnext.tests.utils.ERPNextTestSuite`, and `BootStrapTestData` seeds master data such as companies, items, patients, practitioners, service units, templates and insurance payors, using `_Test ...` names. Call `super().setUp()`.
- **Helpers:** reuse the factory functions other tests export, e.g. `create_appointment` and `update_status` from `test_patient_appointment`, and `make_pos_profile` from ERPNext. Configure `Healthcare Settings` with `frappe.get_single(...).save(ignore_permissions=True)`.
- **Coverage:** CI captures coverage only outside PRs (nightly/push) and uploads it to Codecov. `codecov.yml` sets the project target to `auto` (0.5% threshold) and the **patch target to 85%** on PRs.
- **Labeler:** a PR that changes `healthcare/**/*.py` without touching any `test*.py` gets a `needs-tests` label.
- **Baseline note:** per `wiki/upstream-sync-version-16.md`, the fork `biograph-fh` has no CI test history yet, so the first goal-PR CI run is the baseline.
