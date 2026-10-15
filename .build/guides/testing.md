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
  - healthcare/healthcare/doctype/allergy/test_allergy.py
  - healthcare/tests/utils.py
  - codecov.yml
  - .github/workflows/ci.yml
  - healthcare/hooks.py
---

# Testing

- **Framework**: Frappe integration tests running against a real MariaDB site. Test classes extend `frappe.tests.IntegrationTestCase` (newer) or `frappe.tests.utils.FrappeTestCase` (older). Assertions use unittest-style `assertEqual` and similar.
- **Layout**: `test_<doctype>.py` sits next to its DocType in `healthcare/healthcare/doctype/<name>/`. There are about 110 test files. Cross-cutting helpers live in `healthcare/tests/` (`utils.py` has the `BootStrapTestData` master-data fixtures and uses `erpnext.tests.utils.ERPNextTestSuite`). The `before_tests` hook is `healthcare.healthcare.utils.before_tests`.
- **Data**: tests create their own records through local `create_*` helper functions, using `_Test ...` names. `setUp` often clears tables with `frappe.db.sql("delete from ...")`. Settings are toggled with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- **Many tests are empty stubs** (for example `TestAllergy: pass`). Add real tests when touching a DocType's logic.
- **Running**: `bench --site test_site run-parallel-tests --app healthcare` in CI. Locally, use `bench --site <site> run-tests --app healthcare [--doctype "X"]`.
- **Coverage**: Codecov requires **85% patch coverage** on PRs against `develop`. The project threshold is auto with 0.5% allowed drop. Coverage is captured on scheduled and non-PR runs.
- No frontend (Vue/JS) test suite exists.
