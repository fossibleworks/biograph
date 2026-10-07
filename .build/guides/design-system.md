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
  - patient_portal/src/patient_portal.js
  - patient_portal/vite.config.js
---

- **Desk UI.** Use Frappe Desk's built-in form, list, tree and calendar views, dialogs (`frappe.ui.Dialog`), and HTML templates (`healthcare/public/js/*.html`, e.g. `observation.html` and `healthcare_orders.html`). Do not add a separate CSS framework to Desk.
- **Patient Portal.** **frappe-ui** is both the component library and the token source. Tailwind uses `presets: [frappeUIPreset]` from `frappe-ui/tailwind`, and the only extras are legacy color aliases (lightBlue, warmGray, trueGray, coolGray, blueGray).
  - Globally registered components: `Button`, `Dialog`, `Badge`, `Card`, `Tooltip`, `FeatherIcon`.
  - Icons come from feather-icons and lucide (`lucideIcons: true` in the Vite plugin).
  - Style with Tailwind utility classes from the frappe-ui preset, not custom CSS. `src/index.css` holds the Tailwind entry.
  - Feature components live in `src/components` (e.g. `BookAppointmentModel.vue`, `PractitionerSelector.vue`, `Payment.vue`).
