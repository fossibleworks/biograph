---
title: Design system
category: design-system
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - patient_portal/tailwind.config.js
  - patient_portal/src/patient_portal.js
  - patient_portal/vite.config.js
---

# Design system

## Patient Portal (Vue)
- **frappe-ui** is the component library and token source.
  - `tailwind.config.js` uses `presets: [frappeUIPreset]` from `frappe-ui/tailwind`. The only extensions are a few legacy colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`).
  - Components are registered globally in `src/patient_portal.js`: `Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip`, `Card`. Data fetching uses `frappeRequest` as the `resourceFetcher`.
  - Icons come from feather-icons, with Lucide enabled in the Vite plugin.
- Style with Tailwind utility classes and frappe-ui tokens. Do not introduce a new CSS framework or hard-coded palette. Global styles live in `src/index.css`.
- Existing portal components are in `patient_portal/src/components/`: `AppointmentModel`, `BookAppointmentModel`, `Calendar`, `DepartmentSelector`, `PractitionerSelector`, `DiagnosticModel`, `Payment`. Extend these before adding parallel ones.

## Desk
- Desk screens use Frappe's standard form, list and tree views and Frappe UI controls (`frappe.ui.form`, dialogs). Custom widgets use Jinja HTML templates in `healthcare/public/js/*.html`. Follow Frappe Desk styling rather than custom CSS.
