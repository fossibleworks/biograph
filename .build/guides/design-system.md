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
  - patient_portal/vite.config.js
  - patient_portal/src/components/Payment.vue
  - healthcare/public/js/healthcare.bundle.js
---

# Design system

- **Desk UI** uses standard Frappe Desk widgets: DocType forms, list and tree views, workspaces, number cards and dashboard charts. Custom widgets live in `healthcare/public/js`, e.g. `observation_widget.js`, `healthcare_note.html`, and `healthcare_orders.html` templates.
- **Patient Portal** uses **frappe-ui** as its component library (`Card`, `toast`, and others). It is themed through the **`frappe-ui/tailwind` preset**, which is the design-token source in `patient_portal/tailwind.config.js`.
  - The only local additions are legacy colour aliases: `lightBlue`, `warmGray`, `trueGray`, `coolGray` and `blueGray`.
  - Icons come from feather-icons and lucide (`lucideIcons: true`).
- Style with Tailwind utility classes on the existing grey scale: `text-gray-900` for headings, `text-gray-500` for secondary text, `rounded-xl shadow-sm` cards. Use green and blue accents for amounts.
- Use frappe-ui components in preference to custom HTML. Do not add new CSS frameworks.
