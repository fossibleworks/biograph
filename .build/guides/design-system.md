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
  - patient_portal/src/components/Payment.vue
  - healthcare/public/js/healthcare_note.js
  - healthcare/hooks.py
---

# Design system

- **Desk UI:** use the standard Frappe desk components: `frappe.ui.form`, `frappe.ui.Dialog` with `primary_action_label`, list views, and the tree view (`healthcare_service_unit_tree.js`). Shared widgets live in `healthcare/public/js` (`healthcare_note.js`, `observation_widget.js`, plus `.html` templates). Don't introduce another UI library in desk.
- **Patient portal:** use **frappe-ui** as the component library (`Card`, `Button`, `ErrorMessage`, `toast`, resources) and **Tailwind 3** with the `frappe-ui/tailwind` preset as the token source. `tailwind.config.js` only adds legacy colour aliases (`lightBlue`, `warmGray`, ...). Use Tailwind utility classes such as `text-gray-700`, `text-sm` and `font-semibold`. Icons come from feather / lucide through frappe-ui (`lucideIcons: true`).
- Brand assets live in `healthcare/public/images` (the `healthcare.svg` app logo).
