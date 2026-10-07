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
  - patient_portal/src/components/Payment.vue
  - patient_portal/src/utils/formatters.js
  - patient_portal/vite.config.js
---

**Desk UI** (staff): the standard **Frappe Desk** look. Forms, dialogs (`frappe.ui.Dialog`), list views, workspaces, number cards, and dashboard charts are all defined as metadata (JSON) under `healthcare/healthcare/`. Do not add custom CSS frameworks to Desk. Use Frappe form APIs and indicators (`orange`, `green`, `red`, `blue`).

**Patient Portal** (patients): **frappe-ui** is the component library and token source.
- `patient_portal/tailwind.config.js` uses `presets: [frappeUIPreset]` (`frappe-ui/tailwind`) as the design-token source. Colors, spacing, and typography come from that preset. The config only adds legacy Tailwind color aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`).
- Components: frappe-ui (`Card`, buttons, dialogs, resources like `createDocumentResource`), with icons from feather / lucide (`lucideIcons: true`).
- Styling uses Tailwind utility classes inline in SFCs, e.g. `text-2xl font-bold text-gray-900`, `text-sm text-gray-500`, `p-5 rounded-xl shadow-sm`, and `text-green-600` for amounts. Global CSS is in `patient_portal/src/index.css`.
- Use the formatting helpers in `patient_portal/src/utils/formatters.js` (`formatCurrency` respects System Settings locale and en-IN).

Reuse frappe-ui components and preset tokens. Do not introduce another UI kit or hard-coded hex colors.
