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
  - patient_portal/src/components/Payment.vue
  - healthcare/public/js/healthcare_orders.html
  - healthcare/public/images/biograph-app-icon.svg
---

- **Desk UI** uses the stock Frappe/ERPNext desk with no custom design tokens. Customise forms through DocType JSON, form scripts, `frappe.ui` dialogs and HTML templates in `healthcare/public/js` (`healthcare_orders.html`, `observation.html`, `healthcare_note.html`).
- **Patient Portal:**
  - The component library is **frappe-ui** (`Card`, `ErrorMessage`, `Button`, dialogs, `createResource`).
  - Icons come from `lucideIcons: true` in the vite plugin, plus `feather-icons`.
  - Tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The only extension is legacy colour aliases: `lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`.
  - Components use Tailwind utilities, for example `text-gray-900`, `text-sm text-gray-500`, `rounded-xl shadow-sm`, `p-5`, and `text-green-600` for amounts.
  - Global CSS is in `patient_portal/src/index.css`.
- Brand icons are in `healthcare/public/images` (`biograph-app-icon.svg`, `healthcare.svg`).
