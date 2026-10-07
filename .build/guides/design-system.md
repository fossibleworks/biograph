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
  - patient_portal/src/PatientPortal.vue
---

- **Desk UI** uses Frappe's built-in form, list and calendar views and `frappe.ui` dialogs. There are no custom tokens. Styling comes from Frappe/ERPNext, and doctype layout is defined in the doctype JSON.
- **Patient portal** uses **frappe-ui** as its component library and design tokens. Tailwind uses `presets: [frappeUIPreset]` from `frappe-ui/tailwind`, and only adds legacy color aliases (lightBlue, warmGray, trueGray, coolGray, blueGray). Icons come from feather-icons and lucide (`lucideIcons: true` in the Vite frappe-ui plugin).
- Use frappe-ui components (`Button`, `Dialog`, `createResource`, …) and Tailwind utility classes. Do not add another UI kit or hard-coded CSS. The global stylesheet is `patient_portal/src/index.css`.
