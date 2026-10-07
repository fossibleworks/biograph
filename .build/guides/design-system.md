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
  - patient_portal/src/PatientPortal.vue
---

- **Desk UI** uses stock Frappe Desk forms, dialogs (`frappe.ui.Dialog`), list and calendar views, and doctype-JSON layouts. Don't add custom CSS frameworks there. Small HTML partials live in `healthcare/public/js/*.html` (e.g. `observation.html`, `healthcare_orders.html`).
- **Patient Portal** uses **frappe-ui** as its component library: `Tabs`, `Dialog`, `Button` and similar, plus `createResource` for data. Its Tailwind preset (`frappe-ui/tailwind`) is the token source. `tailwind.config.js` only adds legacy colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`).
- Icons are feather/lucide, enabled through the frappe-ui Vite plugin (`lucideIcons: true`). Dialogs use `icon: { name: 'alert-triangle', appearance: 'warning' }`-style options.
- Portal components are PascalCase SFCs in `patient_portal/src/components/` (`AppointmentModel.vue`, `BookAppointmentModel.vue`, `Calendar.vue`, `Payment.vue`, ...).
- App branding assets are in `healthcare/public/images` (`healthcare.svg`, `biograph-app-icon.svg`).
