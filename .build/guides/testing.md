---
title: Testing
category: testing
layer: project
applies_to: []
inclusion: always
binding: required
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/tests/utils.py
  - codecov.yml
  - .github/workflows/ci.yml
  - healthcare/hooks.py
  - .github/helper/site_config.json
---

- **Framework:** Frappe's test runner on top of unittest. New tests subclass **`frappe.tests.IntegrationTestCase`**, which about 69 test files already use. Older files use `frappe.tests.utils.FrappeTestCase`. Do not use either for new code.
- **Layout:** each DocType has `test_<doctype>.py` next to its controller in `healthcare/healthcare/doctype/<name>/`. There are about 120 test files. Shared helpers live in `healthcare/tests/utils.py` (for example `create_encounter`), which carries a TODO to centralise more of them. Many tests also import factory helpers such as `create_healthcare_docs` and `create_appointment` from sibling test modules.
- **Setup:** `before_tests = healthcare.healthcare.utils.before_tests` in `hooks.py` prepares fixtures. Tests run against a real MariaDB site and commonly clean tables in `setUp` with `frappe.db.sql("delete from ...")`. Test records use the `_Test ...` naming prefix.
- **Running tests:** `bench --site test_site run-parallel-tests --app healthcare` (CI), or `bench run-tests --doctype "<DocType>"` locally.
- **CI:** the `CI` workflow runs server tests on PRs, except PRs that only touch css/js/md/html/csv, and nightly. Coverage is collected on non-PR runs only.
- **Coverage:** Codecov enforces **85% patch coverage** on PRs to `develop`, and project coverage must not drop by more than 0.5%.
- There are no JS or portal unit tests. `cypress/` is referenced only in ignore lists.
- When adding a controller or whitelisted API, add or extend the matching `test_<name>.py`.
