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
  - healthcare/healthcare/doctype/allergy/test_allergy.py
  - .github/workflows/ci.yml
  - codecov.yml
---

# Testing

## Framework
- Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`) against a real MariaDB site that has ERPNext installed.
- All test classes extend **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which subclasses ERPNext's `ERPNextTestSuite`. Recent commits migrated every remaining test to it.
- `BootStrapTestData` in the same file creates shared master data: company, items, departments, patients, practitioners, service units, templates and insurance payors.

## Layout
- Tests sit next to the doctype: `healthcare/healthcare/doctype/<name>/test_<name>.py`, class `Test<DocType>`. There are about 85 test files.
- Some are placeholder stubs (`class TestAllergy(HealthcareTestSuite): pass`).

## Writing tests
- If you override `setUp`, call `super().setUp()`. A recent fix added missing calls.
- Fetch fixtures deterministically, e.g. `frappe.get_list("Patient", pluck="name")[0]`.
- Prefix test records with `_Test `.
- Clean up with `frappe.db.sql("delete from \`tab...\`")` in `setUp` where existing tests already do.
- Toggle settings via `frappe.db.set_single_value("Healthcare Settings", ...)`.
- Assert errors with `self.assertRaises(<SpecificError or frappe.ValidationError>, ...)`.
- Put module-level factory helpers (e.g. `create_appointment(...)`) in the test module.

## Coverage / CI
- CI runs server tests on PRs (ignoring JS/CSS/MD-only changes) and nightly.
- Coverage is uploaded to Codecov on non-PR runs only.
- `codecov.yml` sets a **patch target of 85%** and allows a project drop of at most 0.5%.
- The fork has no CI baseline yet. The first goal-PR run is the baseline (see `wiki/upstream-sync-version-16.md`).
