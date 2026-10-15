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
  - patient_portal/src/components/BookAppointmentModel.vue
  - patient_portal/src/components/AppointmentModel.vue
  - healthcare/public/js/observation_widget.js
---

- **Desk UI:** standard Frappe Desk. DocType forms, list views, workspaces, number cards, dashboard charts and print formats are all metadata (JSON). Custom widgets in `healthcare/public/js` (observation widget, healthcare notes and orders) use Frappe UI controls such as `frappe.ui.Dialog` and field types, plus `.html` microtemplates. Follow Frappe Desk styling and don't add custom CSS frameworks.
- **Patient Portal:** **frappe-ui** is the component library: `Button`, `Dialog`, `Card`, `Badge`, `Progress`, `FeatherIcon`, `createResource`. **Tailwind CSS** uses `frappePUIPreset` (`frappe-ui/tailwind`), which is the source of design tokens: colors such as `text-ink-gray-8`, spacing and radii. `tailwind.config.js` extends only legacy color aliases. Icons are Feather or Lucide through the frappe-ui Vite plugin. Use the frappe-ui semantic tokens (`ink-*`, `surface-*`) and Button `variant` / Badge `theme` props rather than raw hex values.
