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
---

- **Desk UI** (almost all staff screens) uses Frappe's built-in form, list, tree and calendar views, configured through DocType JSON and `frappe.ui.form.on` scripts. Use standard Frappe controls and dialogs (`frappe.ui.Dialog`, `frm.add_custom_button`) before writing custom HTML. Custom HTML snippets live in `healthcare/public/js/*.html` (e.g. `healthcare_orders.html`, `observation.html`).
- **Patient Portal** uses **frappe-ui** as its component library and token source. `tailwind.config.js` uses `presets: [frappeUIPreset]` and only adds legacy colour aliases (lightBlue → sky, warmGray → stone, and so on). Use frappe-ui components and Tailwind utility classes. Do not add new colour scales or another UI kit.
- Icons: frappe-ui lucide icons (`lucideIcons: true` in Vite) and `feather-icons`.
- Global styles are in `patient_portal/src/index.css`.
