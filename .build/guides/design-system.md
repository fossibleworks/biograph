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
  - patient_portal/components.d.ts
  - healthcare/public/js/observation.html
---

The **desk UI** uses the standard Frappe/ERPNext desk.
- Build forms, lists, trees and dashboards from DocType metadata, with `frappe.ui.form` scripts and `frappe.ui.Dialog`.
- Use the HTML templates in `healthcare/public/js/*.html` (observation, healthcare notes and orders widgets) for custom widgets.
- Do not bring in a separate component library for desk screens.

The **Patient Portal** uses **frappe-ui** as its component library and token source.
- `tailwind.config.js` uses `presets: [frappeUIPreset]` from `frappe-ui/tailwind`, and only adds legacy colour aliases (lightBlue→sky, warmGray→stone, and so on).
- Icons come from feather-icons and lucide (`lucideIcons: true` in the Vite plugin).
- Components are auto-imported (`components.d.ts`).
- Build new portal UI from frappe-ui components and Tailwind utility classes. Do not add raw CSS or new colour tokens.
- Global CSS is `patient_portal/src/index.css`.
