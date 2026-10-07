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
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/public/js/observation.js
---

There are two UI surfaces, each with its own source of components and tokens:

**1. Frappe Desk (most of the app)**
- Use Frappe's built-in form, list, report and dialog UI. UI comes from DocType JSON (field types, sections, columns) plus form scripts. Do not add custom CSS frameworks.
- Dialogs use `new frappe.ui.Dialog({ title: __(...), fields: [...], primary_action_label: __(...) })`. Reusable widgets live in `healthcare/public/js` (observation widget, healthcare notes, orders templates as `.html` Jinja/microtemplates).
- Workspaces, number cards, dashboard charts and onboarding are metadata under `healthcare/healthcare/*`.

**2. Patient Portal (Vue SPA)**
- The component library is **frappe-ui** (Button, Dialog, FeatherIcon, resources and so on, imported from `'frappe-ui'`).
- The design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The only additions are legacy color aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Use Tailwind utility classes. Global CSS is in `patient_portal/src/index.css`.
- Icons are feather or lucide (`lucideIcons: true` in the Vite config).
- Components live in `patient_portal/src/components/` with PascalCase names (`BookAppointmentModel.vue`, `Calendar.vue`, `PractitionerSelector.vue`).
