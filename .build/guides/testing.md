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
  - .github/helper/install.sh
---

**Framework:** Frappe's test runner (unittest style) runs inside a bench site. There are 85 `test_*.py` files.

**Layout:** each doctype has a co-located `test_<doctype>.py` next to its controller (for example `healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py`). Shared fixtures and helpers live in `healthcare/tests/utils.py`.

**Base class:** test classes are named `Test<DocType>` and **must subclass `HealthcareTestSuite`** (from `healthcare.tests.utils`), which extends ERPNext's `ERPNextTestSuite`. A recent commit migrated the remaining fork tests to this base. `BootStrapTestData` creates the master data: company, items, departments, patients, practitioners, service units, templates and insurance payors. Records use the `_Test ...` naming prefix.

**Conventions seen in tests**
- Call `super().setUp()` in `setUp` (a recent fix added the missing calls).
- Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
- Use module-level `create_<thing>()` helper functions inside test files.
- Assert validation failures with `self.assertRaises(frappe.ValidationError)` or a specific subclass.
- Prefer deterministic fixtures, for example `frappe.get_list(..., pluck="name")`.

**Running:** CI runs `bench --site test_site run-parallel-tests --app healthcare` on MariaDB 11.8. Fork branches (`biograph-fh`, `goal/*`) are tested against frappe/erpnext `version-16`.

**Coverage:** `codecov.yml` sets the patch target to **85%** (`only_pulls`) and allows the project coverage to drop by at most 0.5%. Coverage is captured only on non-PR (scheduled) runs. The fork has no CI baseline yet (see the wiki sync ledger), so the first CI run on a goal PR is the baseline.
