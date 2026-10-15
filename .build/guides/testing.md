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
  - healthcare/hooks.py
  - codecov.yml
  - .github/labeler.yml
  - .github/workflows/ci.yml
---

**Framework:** Frappe's test runner, which is unittest-based. Test classes subclass `frappe.tests.utils.FrappeTestCase`. Shared fixtures use ERPNext's `ERPNextTestSuite`/`BootStrapTestData` in `healthcare/tests/utils.py`. `hooks.py` registers `before_tests = "healthcare.healthcare.utils.before_tests"` for site setup.

**Layout:**
- Tests sit next to the code: `healthcare/healthcare/doctype/<name>/test_<name>.py`. There are about 110 `test_*.py` files.
- There are also `healthcare/tests/test_utils.py` and `healthcare/regional/india/abdm/test_abdm.py`.
- Tests import ERPNext helpers where needed, for example `make_pos_profile`.

**Style seen in the code:**
- `setUp` often clears tables with `frappe.db.sql("delete from `tab...`")`.
- Module-level factory helpers (`create_healthcare_docs`, `create_appointment`, `create_encounter`) are reused across test modules.
- Settings are toggled with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- Assertions use `self.assertEqual` / `assertTrue`, often against `frappe.db.get_value` after an action.

**Running:** `bench --site test_site run-parallel-tests --app healthcare`, as in CI. CI needs MariaDB plus a full bench with erpnext and payments, which `.github/helper/install.sh` sets up.

**Coverage expectations:**
- Codecov **patch target is 85%** on PRs to `develop`.
- The project status may drop by at most 0.5%.
- Coverage is only collected on scheduled (non-PR) CI runs.
- PRs that change `healthcare/**/*.py` without touching any `test*.py` are auto-labelled **`needs-tests`**.
- The PR template asks for all UI and unit tests to pass locally.

There are no JavaScript or Vue unit tests in the repo.
