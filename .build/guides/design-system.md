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
  - patient_portal/src/index.css
---

- **Desk UI** (practitioners and staff): standard Frappe desk components. Use form scripts, `frappe.ui.Dialog`, list and calendar views, workspaces, number cards and dashboard charts. Don't write custom CSS frameworks.
- **Patient Portal:** **frappe-ui** components (`Card` and others) with **Tailwind CSS** through `frappeUIPreset` (`patient_portal/tailwind.config.js`). The theme extension only aliases legacy Tailwind colour names (lightBlue, warmGray and so on). There are no custom design tokens.
- Icons: feather-icons and lucide (frappe-ui vite `lucideIcons: true`).
- Styling uses Tailwind utility classes in Vue templates: `text-gray-900` headings, `text-gray-500` secondary text, `rounded-xl shadow-sm` cards, green or blue for amounts.
- Components live in `patient_portal/src/components/` as PascalCase SFCs (e.g. `BookAppointmentModel.vue`, `Calendar.vue`, `Payment.vue`).
