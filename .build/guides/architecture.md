---
title: Architecture
category: architecture
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/hooks.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/api/patient_portal.py
  - healthcare/modules.txt
  - healthcare/patches.txt
---

Standard Frappe app layout:

- `healthcare/hooks.py`: the integration hub. It registers `doctype_js` (adds healthcare JS to ERPNext forms), `override_doctype_class` (overrides ERPNext classes such as Sales Invoice and Payment Entry), `doc_events` (hooks into ERPNext document lifecycles), `scheduler_events` (appointment reminders, daily status updates, fee validity, IP billables, expired medication requests), `standard_queries`, `jinja` helpers, and `after_install = healthcare.setup.setup_healthcare`.
- `healthcare/healthcare/` is the single module, "Healthcare" (`modules.txt`):
  - `doctype/<snake_name>/`: one folder per DocType, containing `<name>.json` (schema), `<name>.py` (controller), `<name>.js` (desk form script), and `test_<name>.py`.
  - `custom_doctype/`: overrides of ERPNext doctypes (`sales_invoice.py`, `payment_entry.py`).
  - `api/patient_portal.py`: `@frappe.whitelist()` endpoints that the Vue portal calls.
  - `report/`, `dashboard_chart(_source)/`, `number_card/`, `workspace/`, `page/`, `print_format/`, `web_form/`, `module_onboarding/`: Frappe metadata artifacts.
  - `utils.py`, `healthcare.py`, `auth.py`, `setup/`: shared logic, install-time fixtures and duplicate-check setup.
- `healthcare/controllers/`: shared controllers (`service_request_controller.py`, `queries.py`).
- `healthcare/regional/india/`: country-specific code.
- `healthcare/patches/{v0_0,v15_0,v16_0}` + `patches.txt`: data migrations that run on `bench migrate`.
- `healthcare/public/js`: shared desk JS (bundle, observation widget, healthcare notes, quick entry).
- `healthcare/www/patient_portal.{html,py}` serves the SPA shell. `patient_portal/` holds the Vue source, which builds into `healthcare/public/...`.
- `healthcare/tests/utils.py`: shared test bootstrap (`HealthcareTestSuite`).

**Dependency direction:** healthcare imports from `frappe` and `erpnext`, never the other way round. ERPNext behaviour is extended through hooks and overrides, not by editing ERPNext. Doctype controllers import helpers from each other across doctypes (for example, patient_appointment imports from fee_validity, healthcare_settings and patient_insurance_coverage).
