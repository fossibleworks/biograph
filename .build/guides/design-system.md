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
  - patient_portal/components.d.ts
  - patient_portal/src/components/AppointmentModel.vue
  - healthcare/public/js/observation.js
  - healthcare/public/images/biograph-app-icon.svg
---

- **Desk UI** (most of the product) uses the stock **Frappe desk** components: DocType forms, `frappe.ui.Dialog` (`primary_action_label`), list views, workspaces, number cards and dashboard charts. Build new UI from Frappe form and dialog APIs rather than custom HTML and CSS. Small HTML templates for desk widgets live in `healthcare/public/js/*.html` (e.g. `observation.html`, `healthcare_orders.html`).
- **Patient Portal** uses **frappe-ui** as its component library (Button, Dialog, etc., with typings in `components.d.ts`) and **Tailwind CSS** with the `frappe-ui/tailwind` preset as its token source. `tailwind.config.js` only adds legacy colour aliases (`lightBlue`, `warmGray`, `coolGray`, …). Icons come from `feather-icons` and lucide, enabled through the frappe-ui Vite plugin. Use Tailwind utility classes from the preset (e.g. `text-lg font-semibold text-gray-700`) rather than custom CSS. Global styles are in `patient_portal/src/index.css`.
- App icon and branding assets are in `healthcare/public/images/` (`biograph-app-icon.svg`, `healthcare.svg`).
