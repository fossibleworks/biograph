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
  - patient_portal/vite.config.js
  - patient_portal/package.json
  - patient_portal/src/utils/formatters.js
---

- **Desk UI** (staff): the stock Frappe desk. Forms, list views, dashboards, number cards and workspaces are defined as metadata (doctype JSON, `workspace/`, `number_card/`, `dashboard_chart/`). Custom widgets (observation widget, healthcare notes and orders) use Frappe's built-in styles and HTML templates in `healthcare/public/js/*.html`. There are no custom design tokens.
- **Patient Portal:** **frappe-ui** is the component library (`Button`, `ErrorMessage`, dialogs, etc.) and supplies the design tokens through the Tailwind preset (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The only extension is legacy colour aliases (lightBlue → sky, warmGray → stone, etc.). Icons are feather and lucide (`lucideIcons: true`). Shared formatting lives in `src/utils/formatters.js` (`formatCurrency`).
- Use frappe-ui components and Tailwind utility classes. Do not add new CSS frameworks or one-off colour values.
