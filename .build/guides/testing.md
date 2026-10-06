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
  - healthcare/tests/test_utils.py
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - codecov.yml
  - .github/workflows/ci.yml
---

**Framework:** Frappe's unittest-based test runner, run inside a bench against a MariaDB test site (`bench --site test_site run-parallel-tests --app healthcare`).

**Layout**
- Each DocType has `test_<doctype>.py` next to its controller. There are about 85 test files.
- Shared fixtures live in `healthcare/tests/`:
  - `utils.py` defines `BootStrapTestData` (creates `_Test Company`, items, departments, patients, practitioners, service units, templates, insurance payors and so on) and `HealthcareTestSuite`, which subclasses ERPNext's `ERPNextTestSuite`.
  - `test_utils.py` holds small factory helpers such as `create_encounter`.

**Conventions**
- Test classes are `Test<DocType>(HealthcareTestSuite)`. All fork tests were migrated to this suite, so new tests should use it too.
- Always call `super().setUp()` in `setUp`.
- Test records use the `_Test …` naming prefix.
- Pick records deterministically, for example `frappe.get_list("Patient", pluck="name")[0]`.
- Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- Assert on database state with `frappe.db.get_value`.
- Module-level `create_*` factory functions in the test file build records.
- Do not create companies in before-test hooks. Set the customer group explicitly on test customers.

**Coverage**
- Codecov is configured with a **patch target of 85%** and a project threshold of 0.5%.
- Coverage is captured only on scheduled and non-PR runs (`WITH_COVERAGE` / `CAPTURE_COVERAGE`).

**Baseline caveat:** the fork has no CI history on `biograph-fh`. The first CI run on a goal PR becomes the baseline (see `wiki/upstream-sync-version-16.md`).
