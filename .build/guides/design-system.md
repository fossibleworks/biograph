---
title: Design System
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
  - patient_portal/src/components/Payment.vue
  - patient_portal/src/index.css
  - healthcare/public/js/healthcare_orders.html
---

- **Desk UI (staff):** use the standard Frappe Desk form, list, tree, calendar and dialog components (`frappe.ui.form.on`, `frappe.ui.Dialog`, `frm.add_custom_button`), plus HTML templates in `healthcare/public/js/*.html` and `page/*/` (with page-local `.css`). Build on Frappe's built-in styles rather than adding a separate CSS framework.
- **Patient portal:** **frappe-ui** is the component library (e.g. `Card`, plus frappe-ui resources). **Tailwind CSS 3** is configured with `presets: [frappeUIPreset]` from `frappe-ui/tailwind`, which provides the design tokens. It extends a few legacy colour aliases (`lightBlue`→sky, `warmGray`→stone, `trueGray`→neutral, `coolGray`→gray, `blueGray`→slate). The `content` globs include frappe-ui's components.
- Icons come from feather-icons and lucide, via the frappe-ui vite plugin with `lucideIcons: true`.
- Existing portal styling patterns: neutral grays for text (`text-gray-900` headings, `text-gray-500` secondary text), `rounded-xl shadow-sm` cards, `p-5` padding, and green or blue accents for amounts.
- Global portal CSS lives in `patient_portal/src/index.css`.
