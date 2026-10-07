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
  - healthcare/healthcare/doctype/practitioner_availability/test_practitioner_availability.py
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's unittest-based test runner. Tests run inside a bench site (`bench --site test_site run-parallel-tests --app healthcare`) against MariaDB.
- **Base class:** every test class extends `HealthcareTestSuite`, defined in `healthcare/tests/utils.py` as a subclass of ERPNext's `ERPNextTestSuite`. Fork tests were migrated to it in the B2 upstream sync. `BootStrapTestData` in the same file creates the shared master data (company, items, practitioners, patients, service units, templates, insurance payors…). Test records use the `_Test …` naming prefix.
- **Layout:** place `test_<doctype>.py` next to the controller in `doctype/<name>/`. Other locations: `custom_doctype/test_sales_invoice.py`, `regional/india/abdm/test_abdm.py`, and `healthcare/tests/test_utils.py`. There are about 85 test files.
- **Style:** `setUp` calls `super().setUp()`, then clears relevant tables with `frappe.db.sql("delete from `tab…`")` and toggles settings with `frappe.db.set_single_value(...)`. Module-level helper factories create test docs (e.g. `create_appointment`, `create_encounter`). Validation failures are asserted with `assertRaises(frappe.ValidationError)` or the custom subclass.
- **Coverage:** Codecov sets a **patch target of 85%** on PRs to `develop`, and the project coverage may drop by at most 0.5%. Coverage is captured on scheduled and non-PR runs.
- **Labeler:** a PR that changes `healthcare/**/*.py` without touching any `test*.py` gets the `needs-tests` label.
- No JS or portal test suite exists.
