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
  - patient_portal/src/patient_portal.js
  - patient_portal/vite.config.js
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/public/js/observation_widget.js
---

- **Desk UI** (practitioner and staff screens) uses Frappe's built-in form, list, report, workspace and dashboard components, defined declaratively in doctype JSON and form scripts. Do not add custom CSS frameworks there. Custom widgets (`public/js/observation_widget.js`, `healthcare_note.html`, `healthcare_orders.html`) use Frappe's bundled markup and classes.
- **Patient Portal** uses **frappe-ui** as its component library: `Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip` and `Card` are registered globally in `src/patient_portal.js`.
- **Design tokens** come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The only extras are legacy colour aliases (lightBlue, warmGray, trueGray, coolGray, blueGray).
- Icons come from feather-icons and lucide (the `lucideIcons: true` Vite option).
- Use Tailwind utility classes and frappe-ui components instead of bespoke CSS. Shared formatting helpers live in `patient_portal/src/utils/formatters.js`.
