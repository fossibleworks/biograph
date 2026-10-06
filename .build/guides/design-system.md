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
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/src/components/Payment.vue
  - healthcare/public/js/observation_widget.js
---

- **Desk UI:** the standard Frappe Desk UI. Forms and lists come from the doctype JSON plus `.js` form scripts. Custom widgets live in `healthcare/public/js`, e.g. `observation_widget.js`, `healthcare_note.html`, `healthcare_orders.html`. Do not introduce a separate CSS framework.
- **Patient portal:** the component library is **frappe-ui** (`Button`, `Card`, `ErrorMessage`, resources via `getCachedResource`). Tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The config only adds legacy color aliases (lightBlue, warmGray, ...). Icons are feather and lucide (`lucideIcons: true`).
- Style with Tailwind utilities using the frappe-ui gray scale (`text-gray-800`, `text-gray-600`, `text-sm`/`text-md`). Use Button variants like `variant="subtle"`.
- Global portal styles are in `patient_portal/src/index.css`.
