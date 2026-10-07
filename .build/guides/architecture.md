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
  - healthcare/healthcare/api/patient_portal.py
  - patient_portal/vite.config.js
  - healthcare/patches.txt
  - healthcare/controllers/service_request_controller.py
---

The project is a single Frappe app (`healthcare`) installed into a bench next to frappe, erpnext, and payments.

- `healthcare/hooks.py`: the integration point. It wires `doc_events` (including the wildcard `*` on_submit/on_cancel hooks that build patient medical records), `doctype_js` overrides for ERPNext doctypes (Sales Invoice, Healthcare Practitioner), `scheduler_events` (appointment reminders, daily status updates), jinja methods, `on_login`, and website permissions.
- `healthcare/healthcare/`: the main module.
  - `doctype/<snake_name>/`: about 139 doctypes. Each has a JSON schema, a Python controller (a `Document` subclass), an optional JS form, list, and tree script, and `test_<name>.py`.
  - `api/patient_portal.py`: whitelisted endpoints used by the Vue portal.
  - `utils.py`: shared billing, invoicing, and code helpers.
  - `custom_doctype/`: overrides of ERPNext classes such as Sales Invoice and Payment Entry.
  - `report/`, `page/`, `print_format/`, `dashboard_chart*/`, `number_card/`, `workspace/`, `web_form/`, `setup/`.
- `healthcare/controllers/`: cross-doctype controllers (`service_request_controller.py`, `queries.py`).
- `healthcare/regional/india`: ABDM and other regional code.
- `healthcare/patches/v0_0|v15_0|v16_0` with `patches.txt` (`[pre_model_sync]` and `[post_model_sync]` sections): data migrations.
- `healthcare/setup.py`, `install.py`, `uninstall.py`, `after_migrate.py`: install and setup lifecycle.
- `healthcare/public/js`: desk JS bundle. `healthcare/www`: portal page entry.
- `patient_portal/`: Vue SPA. Vite builds it into `healthcare/public/frontend` and writes the index into `healthcare/www/patient_portal.html`. It calls the Python API over Frappe REST and socket.io.
- `healthcare/tests/utils.py`: `BootStrapTestData` and `HealthcareTestSuite` shared fixtures.

Dependency direction runs healthcare → erpnext → frappe. Import sections follow that order.
