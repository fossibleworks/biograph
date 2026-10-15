---
title: Design System
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
  - patient_portal/src/components/DepartmentSelector.vue
  - patient_portal/src/index.css
  - healthcare/public/js/healthcare_orders.html
---

## Desk UI

The Desk UI uses Frappe's own UI: form scripts, dialogs, `frappe.ui.form`, and the HTML templates in `healthcare/public/js/*.html`. Do not add another component library to Desk.

## Patient Portal

- Components come from **frappe-ui** (`Button`, `Card`, `FeatherIcon`, dialogs, resources).
- Styling uses **Tailwind CSS 3** with `frappeUIPreset` as the token source (`patient_portal/tailwind.config.js`). The only theme extension is legacy colour aliases: `lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`.
- Icons are feather-icons via `FeatherIcon`. lucide icons are enabled in the Vite plugin.
- In existing components, use utility classes rather than custom CSS:
  - Gray palette text: `text-gray-600`, `bg-gray-100`, `border-gray-200`
  - frappe-ui ink tokens: `text-ink-white-7`
  - Shapes: `rounded-xl`, drop-shadows
  - Responsive grids: `grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4`
- Global styles live in `patient_portal/src/index.css` and `healthcare/www/patient-portal/index.css`.
