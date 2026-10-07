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

## Framework

- Frappe's unittest-based runner (`bench run-tests` / `run-parallel-tests`), run against a real MariaDB site.
- Test classes subclass **`HealthcareTestSuite`** from `healthcare/tests/utils.py`, which subclasses ERPNext's `ERPNextTestSuite`. Recent work moved all fork tests onto this base.
- `BootStrapTestData` in the same file builds master data: company, items, departments, users, patients, practitioners, service units, templates, medications, insurance payors and more. Use its `_Test ...` records instead of creating ad-hoc masters.

## Layout

- Put `test_<doctype>.py` next to its doctype in `healthcare/healthcare/doctype/<name>/`. There are about 85 such files.
- Shared helpers go in `healthcare/tests/`.

## Conventions

- Always call `super().setUp()`.
- Clean up with `frappe.db.sql("delete from `tabX`")` or by targeting `_Test %` names.
- Look up existing records with `frappe.get_list(..., pluck="name")`.
- Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- Keep tests deterministic. Many recent commits fix non-deterministic patient and appointment tests.
- Expose module-level `create_*` helpers that other tests can import, e.g. `create_appointment` and `create_encounter`.

## Coverage expectations

- Codecov: project target `auto`, threshold 0.5%. **Patch target 85%** on PRs to `develop`.
- Coverage is collected only on non-PR (scheduled) runs.
- The labeler adds `needs-tests` when a PR changes `healthcare/**/*.py` without touching any `test*.py`.
- Note: the fork branch `biograph-fh` has no CI test baseline yet, per the wiki ledger.
