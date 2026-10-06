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
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

# Design system

- **Desk UI** uses the stock Frappe Desk components: forms, list/tree views, `frm.add_custom_button(__('Label'), fn, __('Group'))`, page indicators (`frm.page.set_indicator(__('Not Saved'), 'orange')`), dialogs, and Jinja print formats. Shared Desk widgets live in `healthcare/public/js/` (observation widget, healthcare notes/orders HTML templates). Don't add custom CSS frameworks to Desk.
- **Patient Portal** uses the **frappe-ui** component library (Button, Dialog, ErrorMessage, toast, createResource, etc.) and the **frappe-ui Tailwind preset** as the design-token source (colors, spacing, typography). `patient_portal/tailwind.config.js` extends it only with Tailwind legacy color aliases (lightBlue, warmGray, trueGray, coolGray, blueGray). Use lucide or feather icons through frappe-ui.
- Style with Tailwind utility classes such as `text-lg font-semibold text-gray-700`. Do not add bespoke CSS files beyond `src/index.css`.
