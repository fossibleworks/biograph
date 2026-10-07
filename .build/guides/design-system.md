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

# Design system

- **Desk UI** (most of the product) uses Frappe Desk's native components: forms, list views, dialogs (`frappe.ui.Dialog`), `frappe.ui.form` controls and indicators. Don't add custom CSS frameworks there. Reuse the widgets in `healthcare/public/js` (observation widget, healthcare notes/orders HTML templates).
- **Patient Portal** uses **frappe-ui** as the component library and design-token source.
  - Tailwind is configured with `presets: [frappeUIPreset]` from `frappe-ui/tailwind`.
  - It adds legacy colour aliases (lightBlue→sky, warmGray→stone, etc.).
  - Icons come from feather-icons/lucide through the frappe-ui vite plugin (`lucideIcons: true`).
  - Global styles are in `patient_portal/src/index.css`.
  - Build new portal UI from frappe-ui components and Tailwind utility classes, not bespoke CSS.
