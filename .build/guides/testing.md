---
title: Testing
category: testing
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/tests/utils.py
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - healthcare/regional/india/abdm/test_abdm.py
  - codecov.yml
  - .github/helper/install.sh
---

- **Framework:** the Frappe test runner (unittest-based). Tests subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on `erpnext.tests.utils.ERPNextTestSuite`. `BootStrapTestData` creates shared master data: company, items, patients, practitioners, service units, templates, and so on.
- **Layout:** each test sits next to its doctype as `doctype/<name>/test_<name>.py`, plus `custom_doctype/test_sales_invoice.py`, `regional/india/abdm/test_abdm.py` and `healthcare/tests/test_utils.py`. The repo has about 85 test files.
- **Style:** `setUp()` calls `super().setUp()`, clears the relevant tables (`frappe.db.sql("delete from `tabX`")`) and toggles `Healthcare Settings` with `frappe.db.set_single_value`. Module-level factory helpers (`create_appointment`, `create_encounter`, ...) build the documents, and assertions use `assertEqual`/`assertTrue` against `frappe.db.get_value`.
- **Running:** `bench --site <site> run-tests --app healthcare` or `--module <dotted.path>`. A bench is required.
- **Coverage:** `codecov.yml` sets a **patch target of 85%** on PRs, and project coverage may not drop by more than 0.5%.
- **CI status:** `.github/helper/install.sh` exists for a test bench, but no `ci.yml` test workflow is currently present in `.github/workflows`. The upstream-sync ledger records that it could not be added because the push credential lacks workflow scope. Run tests locally and report the results in the PR.
- Expect baseline failures on untouched `biograph-fh`. They are recorded in `wiki/upstream-sync-version-16.md`, so compare against that baseline rather than expecting a fully green run.
