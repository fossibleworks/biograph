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
  - patient_portal/vite.config.js
  - patient_portal/src/components/PractitionerSelector.vue
  - healthcare/public/js/observation_widget.js
---

- **Desk UI:** use Frappe desk's built-in components (`frappe.ui.form`, `frappe.ui.Dialog` with `primary_action_label`, list and calendar views). There is no custom token layer, and app CSS is not included (`app_include_css` is commented out).
- **Patient Portal:** the component library is **frappe-ui** (`Button`, `Card`, `createResource`/cached resources, etc.). Styling uses **Tailwind 3.4** with the `frappe-ui/tailwind` preset as the design-token source. `tailwind.config.js` only adds legacy colour aliases (lightBlue, warmGray, …). Icons are feather-icons or Lucide (`lucideIcons: true` in the frappe-ui vite plugin).
- Use frappe-ui button variants and sizes (`variant="subtle"`, `size="sm"`) instead of custom-styled buttons.
