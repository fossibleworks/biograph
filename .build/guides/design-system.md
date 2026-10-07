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
  - patient_portal/vite.config.js
  - patient_portal/src/components/Payment.vue
  - healthcare/public/js/form.js
---

- **Desk UI** uses Frappe's built-in form, list, and dialog components: `frm.add_custom_button`, `frm.page.set_primary_action`, `frappe.ui.Dialog`, and indicators such as `set_indicator(__("Not Saved"), "orange")`. Don't introduce custom CSS frameworks in desk.
- **Patient portal** uses **frappe-ui** as its component library (`Card`, `ErrorMessage`, and others) and **Tailwind** with `frappeUIPreset` as the token source (`patient_portal/tailwind.config.js` only adds legacy color aliases). Icons come from feather and lucide through the frappe-ui Vite plugin.
- Styling uses Tailwind utilities such as `text-gray-900`, `rounded-xl`, and `shadow-sm`. Global CSS lives in `patient_portal/src/index.css`.
