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

- **Framework:** Frappe's unittest-based test runner, run through `bench run-tests` / `run-parallel-tests` against a real MariaDB site.
- **Layout:** tests sit next to the code as `healthcare/healthcare/doctype/<name>/test_<name>.py`. There are 85 test modules. Shared bootstrap code is in `healthcare/tests/utils.py`.
- **Base class:** subclass `HealthcareTestSuite` from `healthcare.tests.utils`. It extends ERPNext's `ERPNextTestSuite`, and `BootStrapTestData` seeds master data: company, items, patients, practitioners, service units, templates and an insurance payor.
- **Pattern:** call `super().setUp()`. Clean tables with `frappe.db.sql("delete from `tabX`")` and pick fixture records from the seeded data (`frappe.get_list(..., pluck="name")[0]`). Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- **Naming:** methods are `test_<behaviour>`. Factory helpers are module-level `create_*`, for example `create_appointment` and `create_encounter`. Test records are prefixed `_Test ` (`_Test Insurance Payor`).
- **Assertions:** `assertEqual`, `assertTrue`, and `assertRaises(frappe.ValidationError)` (or a custom subclass) to check that validation fails.
- **Coverage:** Codecov. Patch target is **85%** on PRs against develop, and the project threshold allows a drop of no more than 0.5%. CI collects coverage only on non-PR (scheduled) runs (`WITH_COVERAGE`).
- **Frontend:** no JS or Vue test suite exists. CI's paths-ignore skips server tests for JS/CSS/MD/HTML-only changes.
