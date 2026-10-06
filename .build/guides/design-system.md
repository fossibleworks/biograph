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
  - healthcare/public/js/healthcare_note.js
  - healthcare/public/images/biograph-app-icon.svg
---

**Desk UI** (staff): use the standard Frappe desk components. Use `frappe.ui.form` for forms, `frappe.ui.Dialog` with `fields` and `primary_action_label` for dialogs (for example `healthcare_note.js`), and `frappe.msgprint` and `frappe.show_alert` for messages. Shared HTML templates live in `healthcare/public/js/*.html`. Do not bring in a separate CSS framework for desk screens.

**Patient Portal** (patients): **frappe-ui** is the component library. It provides `Button`, `Dialog`, `FormControl`, `Select`, `Progress`, `ErrorMessage`, `toast`, and `createResource` for data fetching.
- Design tokens come from the frappe-ui Tailwind preset (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The only extension is legacy Tailwind colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`).
- Styling uses Tailwind utility classes in Vue SFCs. Global CSS is in `patient_portal/src/index.css`.
- Icons are `feather-icons`, which frappe-ui uses.
- Brand assets are in `healthcare/public/images/`: `biograph-app-icon.svg` and `healthcare.svg`.
