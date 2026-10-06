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

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`), run against a real MariaDB site with ERPNext and payments installed.
- **Layout:** each test sits next to its DocType as `healthcare/healthcare/doctype/<name>/test_<name>.py`. There are about 85 Python test files. Custom-doctype tests sit next to their module, for example `custom_doctype/test_sales_invoice.py`. There are no JS or portal tests.
- **Base class:** test classes extend `HealthcareTestSuite` from `healthcare.tests.utils`, which builds on ERPNext's `ERPNextTestSuite`. `BootStrapTestData` creates shared master data: company, items, practitioners, patients, service units, templates and insurance payors, with records named `_Test ...`. Call `super().setUp()`, because recent fixes added missing calls.
- **Patterns:** setUp clears the relevant tables with `frappe.db.sql("delete from `tabX`")`. Fixtures come from `frappe.get_list(..., pluck="name")`. Settings are toggled with `frappe.db.set_single_value`. Module-level `create_*` helpers build documents. Tests should be deterministic; recent commits fixed ordering issues.
- **Expectations:** the labeler adds a `needs-tests` label to PRs that change `healthcare/**/*.py` without touching any `test*.py`. Codecov sets a **patch target of 85%** and allows the project to drop at most 0.5%. Coverage is captured only on the nightly scheduled run, not on PRs.
- **CI:** the `Server Tests` job in `ci.yml` runs on PRs (except css/js/md/html/csv-only changes) and nightly. Fork branches such as `biograph-fh` and `goal/*` install Frappe/ERPNext `version-16`.
