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
  - patient_portal/src/components/BookAppointmentModel.vue
---

- **Patient portal:** uses **frappe-ui** as both component library and token source. `tailwind.config.js` uses `presets: [frappeUIPreset]` and scans frappe-ui components. The only extension is legacy colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Use frappe-ui components (Button, Dialog, Tabs, etc.) and `createResource` for data, with Tailwind utilities for layout. Icons come from feather-icons and lucide through the frappe-ui Vite plugin. Global styles live in `patient_portal/src/index.css`.
- **Desk UI:** uses Frappe Desk's native form, list, calendar and dialog widgets (`frappe.ui.form.on`, `frappe.ui.Dialog`, list view inner buttons) and the standard indicator colours. Custom HTML templates live in `healthcare/public/js/*.html`, for example `observation.html` and `healthcare_orders.html`. Print formats are under `healthcare/healthcare/print_format`.
- Do not introduce another component library or CSS framework.
