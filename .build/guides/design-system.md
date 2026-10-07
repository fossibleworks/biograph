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
  - healthcare/public/js/observation_widget.js
---

- **Desk UI** (most of the product) uses the standard Frappe Desk form, list, report and workspace components, defined through DocType JSON, `workspace/`, `number_card/` and `dashboard_chart/`. Custom widgets live in `healthcare/public/js` (`observation_widget.js`, `healthcare_note.js` with `.html` micro-templates). Don't add a separate CSS framework to Desk.
- **Patient Portal** uses **frappe-ui** as its component library and token source. The Tailwind preset is `frappe-ui/tailwind` (in `patient_portal/tailwind.config.js`), with only legacy color aliases added (`lightBlue`→sky, `warmGray`→stone, and so on). Components in use: `Button`, `Dialog`, `Badge`, `Card`, `FeatherIcon` (feather/lucide icons), `FormControl`, `ErrorMessage`.
- Style with Tailwind utility classes from the frappe-ui preset. Don't add custom CSS variables or a new component library.
