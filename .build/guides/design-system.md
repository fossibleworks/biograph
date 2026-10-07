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
  - patient_portal/src/components/Payment.vue
  - patient_portal/src/index.css
  - healthcare/public/images/biograph-app-icon.svg
---

- **Desk UI:** uses the stock Frappe Desk components (form, list, tree, dialogs, `frm.add_custom_button`, `frm.page.set_indicator`, `frappe.ui.Dialog`). Do not introduce custom CSS frameworks. Shared widgets live in `healthcare/public/js`, e.g. `observation_widget.js`, `healthcare_note.html`, `healthcare_orders.html`.
- **Patient portal:** the component library is **frappe-ui** (`Card`, `Button`, `Dialog`, `createResource`, ...). Design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The config only adds legacy color aliases (lightBlue, warmGray, trueGray, coolGray, blueGray). Icons are lucide/feather through frappe-ui.
- Styling uses Tailwind utility classes with the frappe-ui gray scale: headings `text-gray-900`/`800`, secondary text `text-gray-500`, cards `rounded-xl shadow-sm`, amounts `text-green-600`/`text-blue-600`. Global styles go in `patient_portal/src/index.css`.
- Brand assets: `healthcare/public/images/biograph-app-icon.svg` and `healthcare.svg`.
