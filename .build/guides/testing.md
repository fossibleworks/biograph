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

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`), running against a real MariaDB site that has ERPNext installed.
- **Layout:** put tests next to the code. Each doctype folder has a `test_<doctype>.py` (85 test files). Shared fixtures live in `healthcare/tests/utils.py`.
- **Base class:** every test class must extend **`HealthcareTestSuite`** from `healthcare.tests.utils`. It builds on ERPNext's `ERPNextTestSuite`. Its `BootStrapTestData` creates master data: `_Test Company`, patients, practitioners, service units, templates, insurance payors and more.
  - Always call `super().setUp()`.
  - Look up records deterministically, for example `frappe.get_list("Patient", pluck="name")[0]`.
  - Prefix test records with `_Test`.
  - Module-level helpers (`create_appointment(...)`) build documents.
  - Settings are toggled with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- **Coverage:** Codecov expects **85% patch coverage** on PRs to `develop`. Project coverage may drop by at most 0.5%. CI collects coverage on scheduled and non-PR runs.
- **Labeler:** a PR that touches `healthcare/**/*.py` without touching any `test*.py` gets the `needs-tests` label.
- **Baseline note:** the fork has no CI history on `biograph-fh`, so the first CI run on a goal PR is the baseline. No local bench is assumed to be available.
