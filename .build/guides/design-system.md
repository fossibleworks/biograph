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
  - patient_portal/components.d.ts
  - patient_portal/src/components/Payment.vue
  - healthcare/public/js/observation.html
  - healthcare/public/images/healthcare.svg
---

- **Desk UI** (most screens) uses the standard Frappe Desk form, list, calendar and tree views, driven by DocType JSON. Custom widgets reuse Frappe UI primitives (`frappe.ui.Dialog`, `frappe.ui.form.on`, indicators) and small HTML templates in `healthcare/public/js/*.html` (`healthcare_note.html`, `observation.html`, `healthcare_orders.html`). Do not introduce a separate CSS framework for Desk.
- **Patient Portal** uses **frappe-ui** components (Card, Button, Dialog, etc., auto-imported, see `components.d.ts`) on **Tailwind CSS**. The token source is the `frappe-ui/tailwind` preset in `patient_portal/tailwind.config.js`, which adds only legacy colour aliases (lightBlue, warmGray, trueGray, coolGray, blueGray). Icons come from lucide/feather via the frappe-ui vite plugin.
- Existing visual idiom (e.g. `Payment.vue`): centred flex layouts, `text-gray-900/800/500` text hierarchy, `rounded-xl shadow-sm` cards, `text-green-600` / `text-blue-600` for amounts, `max-w-md` content width.
- App icons live in `healthcare/public/images/` (`healthcare.svg`, `biograph-app-icon.svg`).
