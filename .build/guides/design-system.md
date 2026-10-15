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
  - patient_portal/src/components/Payment.vue
  - patient_portal/src/utils/formatters.js
---

- **Patient portal:** the component library is **frappe-ui** (`Card`, `Button`, `ErrorMessage`, …). Its design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The config only adds legacy color aliases: `lightBlue→sky`, `warmGray→stone`, `trueGray→neutral`, `coolGray→gray`, `blueGray→slate`.
  - Style with Tailwind utility classes such as `text-gray-900`, `text-sm text-gray-500`, `rounded-xl shadow-sm`, `space-y-4`.
  - Icons are feather-icons or lucide (`lucideIcons: true` in vite).
  - Shared formatting helpers live in `patient_portal/src/utils/formatters.js` (e.g. `formatCurrency`).
- **Desk UI:** use standard Frappe Desk form controls, dialogs and HTML templates (`public/js/*.html`, e.g. `observation.html`, `healthcare_orders.html`). Do not add a separate CSS framework.
