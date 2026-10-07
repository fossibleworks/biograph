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
  - patient_portal/src/PatientPortal.vue
  - patient_portal/vite.config.js
  - healthcare/public/js/observation_widget.js
---

- **Patient portal:** use the **frappe-ui** component library: `Tabs`, `Dialog`, `createResource`, and the buttons with `variant: 'solid'`.
- **Design tokens** come from the `frappe-ui/tailwind` preset in `patient_portal/tailwind.config.js`. The config only extends legacy colour aliases (lightBlue→sky, warmGray→stone, and so on). Style with Tailwind utility classes, use feather/lucide icons (`lucideIcons: true`), and keep base styles in `src/index.css`.
- **Desk UI** uses the Frappe Desk widgets: `frappe.ui.Dialog`, form buttons, and `.html` templates in `public/js` such as `observation.html` and `healthcare_orders.html`. Use those rather than a custom component library.
