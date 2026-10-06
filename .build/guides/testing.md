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
  - .github/workflows/ci.yml
  - healthcare/healthcare/custom_doctype/test_sales_invoice.py
---

- **Framework:** Frappe's unittest-based test runner. Run it with `bench --site test_site run-parallel-tests --app healthcare` (CI) or `bench run-tests`.
- **Base class:** test classes extend `HealthcareTestSuite` from `healthcare/tests/utils.py`, which subclasses ERPNext's `ERPNextTestSuite`. Remaining fork tests were migrated to this base during the upstream sync. `BootStrapTestData` in the same file creates the shared master data: company, items, patients (`_Test ...` names), practitioners, service units, templates, insurance payors and more.
- **Layout:** one `test_<doctype>.py` next to each doctype controller (`healthcare/healthcare/doctype/<name>/test_<name>.py`). There are about 85 test files. Shared helpers live in `healthcare/tests/`. Custom-doctype tests sit beside their overrides (`custom_doctype/test_sales_invoice.py`).
- **Style:** `setUp()` calls `super().setUp()`, then resets state with `frappe.db.sql("delete from `tabX`")` and toggles settings with `frappe.db.set_single_value("Healthcare Settings", ...)`. Records come from module-level `create_*` helpers. Assertions use `assertEqual` / `assertRaises` with the specific `frappe.ValidationError` subclasses.
- **Determinism:** recent fixes made patient initialisation deterministic. Avoid depending on record order unless the test seeds it.
- **Coverage:** `codecov.yml` requires **85% patch coverage** on PRs. The project threshold is auto with 0.5% tolerance. Coverage is captured on scheduled and non-PR runs.
- **Baseline note:** the fork's `ci.yml` has no run history yet. The first CI run on a goal PR serves as the baseline.
