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
  - healthcare/public/js/observation.html
---

- **Desk (staff UI):** standard Frappe desk with Frappe form/list/tree/calendar views, defined by DocType JSON and `*.js` form scripts. HTML snippets (`healthcare_note.html`, `observation.html`, `healthcare_orders.html`) render inside forms. Use Frappe UI primitives (`frappe.ui.Dialog`, `frappe.msgprint`, indicators) instead of custom CSS.
- **Patient Portal:** **frappe-ui** is the component library and design-token source. `tailwind.config.js` uses `presets: [frappeUIPreset]` and only adds legacy color aliases (`lightBlue`, `warmGray`, …). Components such as `createResource`, Button, Dialog, and lists come from `frappe-ui`. Icons come from lucide/feather through the frappe-ui Vite plugin.
- Portal components live in `patient_portal/src/components` and are named `PascalCase.vue` (`BookAppointmentModel.vue`, `PractitionerSelector.vue`, `Calendar.vue`). Styling uses Tailwind utility classes. Global CSS is limited to `src/index.css`.
