---
title: Testing
category: testing
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/doctype/fee_validity/test_fee_validity.py
  - healthcare/tests/utils.py
  - healthcare/tests/test_utils.py
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
  - healthcare/hooks.py
---

- **Framework:** Frappe's integration test runner. Tests subclass `frappe.tests.IntegrationTestCase` and run against a real MariaDB site with ERPNext installed.
- **Layout:** co-locate tests as `test_<doctype>.py` inside each doctype folder (~130 test files). Cross-cutting helpers live in `healthcare/tests/utils.py` (e.g. `create_encounter`), which a TODO marks as the place to consolidate helpers. Many tests reuse factory helpers from other test modules (e.g. `create_appointment`, `create_healthcare_docs` from `test_patient_appointment.py`).
- **Fixtures:** `EXTRA_TEST_RECORD_DEPENDENCIES = ["Company"]`. `setUp` often clears tables with `frappe.db.sql("delete from `tabX`")` and sets `Healthcare Settings` values directly. `before_tests` in hooks points to `healthcare.healthcare.utils.before_tests`.
- **Run:** `bench --site test_site run-parallel-tests --app healthcare` (CI) or `bench run-tests --app healthcare --doctype "<DocType>"`.
- **Coverage expectations:** Codecov sets the **patch target to 85%** on PRs to `develop`. The project threshold is auto with 0.5% allowed drop. CI captures coverage only on non-PR (scheduled) runs.
- The PR labeler adds `needs-tests` when `healthcare/**/*.py` changes without any `test*.py` change. Add or extend a test with every Python change.
- CI ignores PRs that only touch `.js/.css/.md/.html/.csv`, so JS-only changes get no server tests.
