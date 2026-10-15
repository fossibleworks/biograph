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
  - patient_portal/src/patient_portal.js
  - patient_portal/src/components/Payment.vue
  - patient_portal/vite.config.js
---

# Design system

## Desk UI
Use Frappe desk's built-in components: form layouts defined in DocType JSON, `frappe.ui.form`, `frappe.ui.Dialog`, `frappe.msgprint`, and `frappe.show_alert` with `indicator` colours (`green`, `warning`, …). Do not add custom CSS frameworks to desk pages. Workspaces, number cards and dashboard charts are configured through JSON.

## Patient portal
- The component library is **frappe-ui**. `Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip` and `Card` are registered globally in `patient_portal.js`, and `ErrorMessage` and others are imported per component.
- Design tokens come from **Tailwind** using `frappe-ui/tailwind` as the preset in `patient_portal/tailwind.config.js`. The only extensions are legacy colour aliases (`lightBlue`, `warmGray`, `coolGray`, …).
- Styling uses Tailwind utilities directly in templates (`text-gray-900`, `rounded-xl`, `shadow-sm`). Global CSS lives in `src/index.css`.
- Icons come from feather-icons, plus lucide through the frappe-ui Vite plugin (`lucideIcons: true`).

Before adding a new primitive, reuse the frappe-ui component.
