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
  - healthcare/public/js/mark_unavailable.js
---

# Design system

## Patient Portal (`patient_portal/`)
- The component library is **frappe-ui** (`frappe-ui ^0.1.176`). Use its components (Button, Dialog, FormControl, etc.) and `createResource` / `call` before writing custom ones.
- Design tokens come from **Tailwind CSS 3.4 with `frappe-ui/tailwind` preset** (`presets: [frappeUIPreset]`). The only local extension is legacy colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Use Tailwind utility classes. Do not add ad-hoc CSS or hard-coded colours.
- Icons: `lucideIcons: true` in the frappe-ui vite plugin, plus `feather-icons`.
- Components live in `patient_portal/src/components/` as PascalCase `.vue` files (`BookAppointmentModel.vue`, `PractitionerSelector.vue`, `Calendar.vue`). Global styles are in `src/index.css`.

## Desk UI
- Desk uses Frappe's standard form, list and tree views, configured through doctype JSON and `<doctype>.js` form scripts. Custom widgets (`observation_widget.js`, `healthcare_orders.html`, `healthcare_note.html`) live in `healthcare/public/js` and use Frappe UI classes and `frappe.ui.Dialog`.
