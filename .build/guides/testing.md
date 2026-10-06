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
  - .github/workflows/ci.yml
  - codecov.yml
  - .github/labeler.yml
---

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`) against a real MariaDB-backed site. Base class: `HealthcareTestSuite` from `healthcare/tests/utils.py`, which builds on `erpnext.tests.utils.ERPNextTestSuite`.
- **Fixtures:** `BootStrapTestData` in `healthcare/tests/utils.py` creates master data once: company, service items, patients, practitioners, service units, appointment types, lab/observation templates, therapy types, medications, insurance payors, and so on. Test records use a `_Test ` prefix (`"_Test Insurance Payor"`). Tests usually call `super().setUp()`, clear the relevant tables, and read seeded records with `frappe.get_list(..., pluck="name")`.
- **Layout:** each test sits next to its doctype as `doctype/<name>/test_<name>.py`, with class `Test<DocTypeName>` and methods `test_*`. Module-level helper factories such as `create_appointment(...)` and `create_encounter(...)` are reused across tests.
- **Assertions:** `self.assertEqual`, plus `self.assertRaises(frappe.ValidationError)` (or a specific subclass) for validation paths. Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- **Coverage expectations:** Codecov sets a **patch target of 85%** on PRs and allows the project to drop at most 0.5%. Coverage is captured on scheduled/non-PR CI runs. The labeler adds `needs-tests` to any PR that changes `healthcare/**/*.py` without touching a `test*.py` file.
- **Baseline caveat:** according to `wiki/upstream-sync-version-16.md`, the fork has never run `ci.yml` and the sync environment has no local bench. The first CI run on a PR serves as the baseline.
