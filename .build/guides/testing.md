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
  - healthcare/healthcare/doctype/patient/test_patient.py
  - healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py
  - codecov.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`), which runs against a real site and database.
- **Layout:** tests sit next to the code as `test_<doctype>.py` inside each DocType folder (about 85 test files). Cross-cutting tests live in `healthcare/tests/`, regional ones in `healthcare/regional/india/abdm/test_abdm.py`, and the Sales Invoice override test in `custom_doctype/test_sales_invoice.py`.
- **Base class:** test classes subclass `HealthcareTestSuite` from `healthcare/tests/utils.py`. It builds on ERPNext's `ERPNextTestSuite`, and `BootStrapTestData` seeds master data such as the company, items, practitioners, service units and templates.
- **Fixtures:** reuse helper factories from sibling tests, for example `create_patient` from `test_patient_appointment.py`, and `_Test ...` named records. Toggle settings with `frappe.db.set_single_value`.
- **Assertions:** `self.assertEqual`, `assertTrue`, `assertRaises(<SpecificError>)`.
- **Coverage:** codecov requires **85% patch coverage** on PRs (against `develop`). Project coverage may drop by at most 0.5%. CI uploads coverage artifacts from each parallel container.
- CI skips server tests for PRs that change only `.js`, `.css`, `.md`, `.html` or `.csv` files. There are no JS/Vue unit tests.
- The fork has no CI baseline yet (see `wiki/upstream-sync-version-16.md`). Treat known pre-existing failures as baseline and do not count them as regressions.
