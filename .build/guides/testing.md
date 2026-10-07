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
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`). It runs against a real MariaDB site (`test_site`). No JS/Vue test suite exists.
- **Layout:** tests sit next to the code as `test_<doctype>.py` inside each DocType folder (~85 files). Shared fixtures live in `healthcare/tests/utils.py`.
- **Base class:** subclass `HealthcareTestSuite` from `healthcare.tests.utils`. It builds on ERPNext's `ERPNextTestSuite`, and `BootStrapTestData` creates `_Test Company`, patients, practitioners, service units, templates, insurance payors, and so on. Test records use the `_Test ` prefix.
- **Patterns:** call `super().setUp()`, clear relevant tables with `frappe.db.sql("delete from `tab<DocType>`")`, toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`, use module-level `create_*` helper functions, and check validation with `self.assertRaises(frappe.ValidationError)`.
- **Coverage:** Codecov reports project coverage (auto target, 0.5% threshold) and a **patch target of 85%** on PRs to `develop`. Coverage is only captured on non-PR (scheduled) CI runs.
- **CI:** `ci.yml` runs server tests on PRs that touch more than CSS/JS/MD/HTML/CSV, plus nightly. The fork has no historical CI baseline, so the first goal-PR run serves as the baseline (see `wiki/upstream-sync-version-16.md`).
