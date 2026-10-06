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
  - patient_portal/src/PatientPortal.vue
  - patient_portal/vite.config.js
---

- **Desk UI** (most screens): standard Frappe desk components only. DocType forms are defined in JSON, with `frappe.ui.Dialog` field definitions (`fieldtype`, `label: __()`) and `frappe.show_alert` indicators (`blue`, `green`, `red`, `orange`). Shared widgets live in `healthcare/public/js/` (observation widget, healthcare notes and orders HTML templates, patient quick entry). There is no custom CSS token file. `app_include_css` is commented out.
- **Patient Portal:** the **frappe-ui** component library (`Tabs`, `Dialog`, `Button`, `createResource`, …) with **Tailwind CSS 3** using `presets: [frappeUIPreset]` from `frappe-ui/tailwind`. That preset is the design-token source. `tailwind.config.js` only adds legacy color aliases (lightBlue, warmGray, trueGray, coolGray, blueGray). Icons come from feather-icons and lucide, enabled in the frappe-ui vite plugin.
- Build new portal UI from frappe-ui components and Tailwind utility classes. Do not add a separate component library or hard-coded colors.
