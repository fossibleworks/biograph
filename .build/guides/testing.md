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
  - healthcare/tests/test_utils.py
  - .github/workflows/ci.yml
  - codecov.yml
---

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`), run against a real MariaDB site (`test_site`).
- **Layout:** each doctype has `test_<doctype>.py` next to its controller (85 test files). Shared fixtures live in `healthcare/tests/utils.py`.
- **Base class:** test classes **must** subclass `HealthcareTestSuite` from `healthcare.tests.utils`, which extends ERPNext's `ERPNextTestSuite`. The fork recently migrated all its tests to it ("migrate remaining fork tests to HealthcareTestSuite"). If you override `setUp`, call `super().setUp()`.
- **Fixtures:** `BootStrapTestData` creates master data: company, items, departments, patients, practitioners, service units, templates, insurance payors. Test record names use the `_Test ` prefix, for example `_Test Insurance Payor`.
- Look records up deterministically with `frappe.get_list(..., pluck="name")`. Settings are toggled with `frappe.db.set_single_value("Healthcare Settings", ...)`. Module-level `create_*` helpers (such as `create_appointment`) are reused across test modules.
- **Coverage:** codecov requires an **85% patch target** on PRs (`only_pulls`) and allows project coverage to drop by at most 0.5%. Coverage is captured only on non-PR (scheduled) CI runs.
- **CI:** `Server Tests` runs on pull requests that change something other than css/js/md/html/csv, and nightly. There is no JS or portal test suite.
- **Baseline caveat:** the fork had no CI history before the upstream sync. The first CI run on a goal PR is the baseline (see the wiki ledger).
