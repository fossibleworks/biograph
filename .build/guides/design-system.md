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
  - patient_portal/package.json
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

- **Desk UI** (the main clinical UI) uses Frappe's built-in Desk components: form scripts, `frm.add_custom_button`, `frm.page.set_indicator`, `frappe.ui.Dialog`, and `frappe.show_alert` with indicator colours (`orange`, `green`, `red`). Shared widgets live in `healthcare/public/js/` (observation widget, healthcare notes, orders templates in `.html`). Do not introduce a separate CSS framework in Desk.
- **Patient Portal** uses **frappe-ui** (Vue 3 component library) as its component source. Design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The only extensions are legacy colour aliases (lightBlue → sky, warmGray → stone, …). Icons are feather-icons and lucide (`lucideIcons: true`).
- Components live in `patient_portal/src/components/` and are PascalCase `.vue` files (`BookAppointmentModel.vue`, `PractitionerSelector.vue`).
