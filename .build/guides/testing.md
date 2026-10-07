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

**Framework:** Frappe's test runner, with unittest-style classes extending **`HealthcareTestSuite`** (`healthcare/tests/utils.py`). That class extends ERPNext's `ERPNextTestSuite`. `BootStrapTestData` in the same file creates the master data: company, service items, patients, practitioners, service units, appointment types, lab and observation templates, therapy types, and so on.

**Layout:** tests sit next to the code as `healthcare/healthcare/doctype/<doctype>/test_<doctype>.py` (about 85 test files). Shared helpers are in `healthcare/tests/`.

**Patterns in existing tests**
- `setUp()` calls `super().setUp()`, then clears the relevant tables, e.g. ``frappe.db.sql("delete from `tabPatient Appointment`")``.
- Fetch fixtures from bootstrapped data: `frappe.get_list("Patient", pluck="name")[0]`.
- Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- Module-level factory helpers (`create_appointment`, `create_encounter`, …) are imported by other tests.
- Assert with `self.assertEqual`, `self.assertTrue`, and `self.assertRaises(<CustomError>)`.

**Running:** `bench --site test_site run-parallel-tests --app healthcare` in CI. Locally, use `bench run-tests --app healthcare --doctype "<DocType>"`.

**Coverage expectations**
- Codecov **patch target 85%** on PRs to `develop`. The project target is auto, with a 0.5% threshold.
- Coverage is captured only on scheduled (non-PR) CI runs.
- The PR labeler adds **`needs-tests`** when `healthcare/**/*.py` changes but no `test*.py` does. Add or extend the DocType's test file with every behaviour change.

**Caveat:** the fork has no CI baseline. The first CI run on a goal PR becomes the baseline, per the sync ledger.
