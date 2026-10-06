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
  - healthcare/healthcare/custom_doctype/test_sales_invoice.py
  - codecov.yml
  - .github/workflows/ci.yml
---

- **Framework:** Frappe's unittest-based test runner. Tests run inside a bench site (`test_site`) with ERPNext installed. CI uses `bench --site test_site run-parallel-tests --app healthcare`.
- **Layout:** tests sit next to their code as `test_<doctype>.py` in the doctype directory (about 85 files), e.g. `healthcare/healthcare/doctype/patient_appointment/test_patient_appointment.py`. ERPNext-override tests sit next to the override (`custom_doctype/test_sales_invoice.py`).
- **Base class:** extend `healthcare.tests.utils.HealthcareTestSuite`, which builds on ERPNext's `ERPNextTestSuite`. `BootStrapTestData` creates shared master data: company, items, patients, practitioners, service units, templates and insurance payors. Test records use a `_Test ` name prefix.
- **Pattern:** `setUp()` calls `super().setUp()`, cleans the relevant tables and picks existing fixtures (`frappe.get_list("Patient", pluck="name")[0]`). Module-level helper factories such as `create_appointment(...)` and `create_encounter(...)` build documents. Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`. Assert with `assertEqual` and `assertRaises(<SpecificError>)`.
- **Coverage:** Codecov sets a **patch target of 85%** on PRs to `develop` and lets project coverage drop by at most 0.5%. Coverage is captured only on non-PR (scheduled) CI runs.
- **Fork note:** `biograph-fh` has no CI baseline. The first CI run on a goal PR becomes the baseline, and any failure should be traced to the commit that introduced it.
- New behaviour, especially bug fixes picked from upstream, should come with or keep a `test_*` method in the doctype's test file.
