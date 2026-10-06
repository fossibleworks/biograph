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
  - patient_portal/package.json
  - healthcare/public/js/healthcare_note.js
---

- **Desk UI** uses stock Frappe Desk components: `frappe.ui.Dialog`, form scripts and list/calendar views. Custom HTML templates live in `healthcare/public/js/*.html` (healthcare_note, healthcare_orders, observation), and widgets are in `observation_widget.js` and `form.js`. Do not introduce a separate CSS framework in Desk.
- **Patient portal** uses the **frappe-ui** component library (`Tabs`, `Dialog`, `Button`, `createResource`, and others), with **Tailwind CSS 3** on `frappe-ui/tailwind` as the preset. That preset is the design-token source for colours, spacing and typography. `tailwind.config.js` only adds legacy colour aliases (lightBlue→sky, warmGray→stone, trueGray→neutral, coolGray→gray, blueGray→slate).
- Icons come from Feather and Lucide, enabled with `lucideIcons: true` in the frappe-ui Vite plugin. Dialog icons use names like `alert-triangle` with an `appearance` of warning or similar.
- Global portal styles are in `patient_portal/src/index.css`. Prefer Tailwind utility classes in templates.
