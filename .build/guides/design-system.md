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
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/public/images/biograph-app-icon.svg
---

- **Desk UI** uses the standard Frappe desk components: form scripts, `frappe.ui.Dialog`, `frappe.msgprint`, list and calendar views. Do not introduce custom CSS frameworks there.
- **Patient portal** uses **frappe-ui**:
  - Components: `Dialog`, `Progress`, and others.
  - Styling: Tailwind 3 with `frappeUIPreset` (`patient_portal/tailwind.config.js`). Token classes include `text-ink-gray-8`.
  - Icons: Lucide/feather, enabled through the frappe-ui vite plugin.
  - Tailwind's legacy color aliases are mapped in `tailwind.config.js`: lightBlue, warmGray, trueGray, coolGray, blueGray.
- Portal components live in `patient_portal/src/components/` as PascalCase `.vue` files (`BookAppointmentModel.vue`, `PractitionerSelector.vue`). Shared formatters are in `src/utils/formatters.js`.
- App branding assets are in `healthcare/public/images/` (`biograph-app-icon.svg`, `healthcare.svg`).
