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
---

- **Desk UI** (most screens) is standard Frappe desk: DocType forms, list and tree views, workspaces, dashboards and number cards. It is defined through DocType JSON and `frappe.ui.form` scripts.
  - Do not build custom CSS frameworks for desk.
  - Shared HTML widgets live in `healthcare/public/js` (`observation.html`, `healthcare_note.html`, `healthcare_orders.html`).
- **Patient Portal** uses **frappe-ui** (^0.1.176) as its component library, with **Tailwind CSS 3.4.15** set up through `presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`.
  - The only custom tokens are legacy color aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`) mapped to Tailwind palettes.
  - Icons are feather-icons, with lucide enabled through the frappe-ui Vite plugin (`lucideIcons: true`).
  - Use frappe-ui components and Tailwind utility classes rather than new CSS. The global stylesheet is `patient_portal/src/index.css`.
