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

# Testing

- **Framework:** Frappe/ERPNext integration tests (unittest style) that run against a real MariaDB site through bench. There are no frontend tests.
- **Base class:** `HealthcareTestSuite` from `healthcare.tests.utils`. It extends `erpnext.tests.utils.ERPNextTestSuite`, and `BootStrapTestData` seeds the master data (company, items, patients, practitioners, service units, templates, ...). Recent commits migrated every fork test onto it. New tests must subclass it; don't use `FrappeTestCase` directly.
- **Layout:** put `test_<doctype>.py` next to the doctype, in `healthcare/healthcare/doctype/<dt>/` (about 85 test files). Helpers such as `create_appointment(...)` live as module-level functions in the test file.
- **Patterns:**
  - Call `super().setUp()`.
  - Clean the tables you touch with `frappe.db.sql("delete from `tabX`")`.
  - Toggle settings with `frappe.db.set_single_value("Healthcare Settings", ...)`.
  - Pull fixture records with `frappe.get_list(..., pluck="name")`.
  - Assert on DB state with `frappe.db.get_value`.
  - Keep tests deterministic; recent fixes removed order-dependence.
- **CI:**
  - `run-parallel-tests` runs on PRs that change Python or JSON. It ignores `.js`, `.css`, `.md`, `.html` and `.csv`.
  - It also runs nightly, and collects coverage on non-PR runs.
- **Coverage:**
  - Codecov's **patch target is 85%**; the project status may drop by at most 0.5%.
  - The labeler adds `needs-tests` to PRs that change `healthcare/**/*.py` with no `test*.py` change.
- The fork has no CI baseline yet (see the wiki ledger). The first goal-PR CI run is the baseline, so attribute any failures to the commit that caused them.
