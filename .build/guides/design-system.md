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
  - patient_portal/src/components/Payment.vue
---

- **Patient Portal (Vue):** the component library is **frappe-ui** (`Card`, `ErrorMessage`, `Button`, …, auto-imported through unplugin). Design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]`). The local config only adds legacy color aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Icons are feather-icons and lucide (`lucideIcons: true`). Style with Tailwind utility classes. The existing look uses `text-gray-900/800/500` text, `rounded-xl shadow-sm` cards, and `space-y-*` stacks, with green/blue accents for amounts. Global CSS lives in `patient_portal/src/index.css`.
- **Desk UI:** standard Frappe Desk form, list and dialog components (`frappe.ui.form`, `frappe.ui.Dialog`) with small HTML partials in `healthcare/public/js/*.html` (e.g. `observation.html`, `healthcare_orders.html`). Don't introduce a separate CSS framework into the desk.
