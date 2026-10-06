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
  - healthcare/public/js/healthcare_orders.html
---

- **Desk UI** (most screens) uses the stock **Frappe desk** components. Forms are defined in doctype JSON. Form scripts use `frm.add_custom_button(__("…"), fn, __("Group"))`, `frm.page.set_indicator(__("…"), "orange")`, `frappe.ui.form` dialogs and Frappe indicator colours. Custom HTML snippets live in `healthcare/public/js/*.html` (e.g. `healthcare_orders.html`, `observation.html`). Don't add a separate CSS framework to desk.
- **Patient Portal** uses **frappe-ui** as its component library and design-token source. `tailwind.config.js` applies `presets: [frappeUIPreset]` and only adds legacy colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Icons come from feather-icons or lucide (the frappe-ui vite plugin sets `lucideIcons: true`). Components live in `patient_portal/src/components/*.vue`, named in PascalCase (e.g. `BookAppointmentModel.vue`, `PractitionerSelector.vue`).
- Use frappe-ui components and Tailwind utility classes from the preset, not custom CSS. Global styles belong in `patient_portal/src/index.css`.
