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
---

- **Desk UI** (staff): use Frappe Desk's standard form, list, tree and calendar views, configured through DocType JSON and form scripts. Do not add a custom CSS framework there. Small HTML templates live in `healthcare/public/js/*.html` (e.g. `healthcare_note.html`, `observation.html`).
- **Patient portal:** uses **frappe-ui** as its component library (`Button`, `toast`, dialogs, etc.) and **Tailwind CSS 3.4** with the `frappe-ui/tailwind` preset as the token source. `tailwind.config.js` adds only legacy color aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Icons come from `feather-icons` and Lucide, via the frappe-ui vite `lucideIcons` option.
- Build new portal UI from frappe-ui components and Tailwind utilities (`text-lg font-semibold text-gray-700`). Do not hand-write CSS. Global styles are in `patient_portal/src/index.css`.
