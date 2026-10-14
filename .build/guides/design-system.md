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
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/vite.config.js
---

# Design system

## Desk (staff UI)
This uses the standard **Frappe Desk** UI. Forms, list views, tree views, workspaces, number cards, and dashboard charts are all defined through DocType JSON and Frappe JS APIs (`frappe.ui.form.on`, `frappe.ui.Dialog`, `frappe.show_alert`). Use Frappe's built-in controls and indicators (`indicator: "orange"` / `"green"`) instead of custom CSS. App icons live in `healthcare/public/images/` (`healthcare.svg`, `biograph-app-icon.svg`).

## Patient portal
- The component library is **frappe-ui** (`Button`, `Card`, `ErrorMessage`, `Dialog`, …). Use props such as `variant="subtle"`, `theme="gray"`, and `size="sm"|"md"`.
- Design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The config only adds legacy colour aliases (lightBlue, warmGray, trueGray, coolGray, blueGray).
- Icons are feather-icons and lucide (enabled through the frappe-ui vite plugin `lucideIcons: true`).
- Global CSS lives in `patient_portal/src/index.css`.

Do not add another component library or a custom token set. Extend through the frappe-ui preset.
