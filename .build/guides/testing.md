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

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`). It runs against a real MariaDB site (`test_site`).
- **Layout:** tests sit next to the code as `test_<module>.py`. That means `doctype/<name>/test_<name>.py`, `report/<name>/test_<name>.py`, `custom_doctype/test_sales_invoice.py` and `regional/india/abdm/test_abdm.py`. There are about 85 test files.
- **Base class:** subclass `HealthcareTestSuite` from `healthcare.tests.utils`. It builds on ERPNext's `ERPNextTestSuite`, and `BootStrapTestData` seeds the master data (company, items, patients, practitioners, service units, templates). Call `super().setUp()`.
- **Style:**
  - Use module-level factory helpers such as `create_appointment(...)` and `create_encounter(...)`.
  - Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
  - Use `assertEqual` on persisted values via `frappe.db.get_value`.
  - Clean up in `setUp` with `delete from \`tabX\``.
  - Test validation failures with `self.assertRaises(SpecificError)`.
- **Coverage:** Codecov requires **85% patch coverage** on PRs to `develop` and allows the project coverage to drop by at most 0.5%. Coverage is only captured on non-PR (scheduled) runs.
- **Labeling:** a PR that changes `healthcare/**/*.py` without touching any `test*.py` gets the `needs-tests` label.
- In this fork, `ci.yml` has no run history, so the first CI run on a goal PR becomes the baseline (see the wiki sync ledger).
