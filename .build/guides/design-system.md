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
  - patient_portal/src/PatientPortal.vue
  - patient_portal/vite.config.js
---

- **Patient Portal:** the component library is **frappe-ui**. Components such as `Button`, dialogs and resources are imported from `'frappe-ui'`, and button styling uses props like `variant='subtle'` and `size='sm'`. Styling uses **Tailwind CSS 3.4** with the `frappe-ui/tailwind` preset as the token source. `tailwind.config.js` adds only legacy color aliases (lightBlue→sky, warmGray→stone, and so on). Icons are feather-icons, plus lucide through the frappe-ui vite plugin (`lucideIcons: true`). Global CSS is in `patient_portal/src/index.css`.
- **Desk UI:** use the standard Frappe desk widgets (`frappe.ui.form`, dialogs, `frappe.msgprint`), Jinja HTML templates in `healthcare/public/js/*.html` (for example `observation.html` and `healthcare_orders.html`), and print formats under `healthcare/healthcare/print_format`.
- Do not introduce another component library or a custom token set. Reuse frappe-ui components and the preset's Tailwind classes.
