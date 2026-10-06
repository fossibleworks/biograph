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
  - patient_portal/src/components/Payment.vue
  - healthcare/hooks.py
  - healthcare/public/js/observation.html
---

- **Desk UI** (most screens) uses the **Frappe desk** components: DocType forms, list views, dialogs (`frappe.ui.Dialog`), `frappe.msgprint`, workspaces, number cards and dashboard charts. Look comes from Frappe/ERPNext. There is no custom CSS bundle (`app_include_css` is commented out). HTML snippets for widgets live in `healthcare/public/js/*.html` (healthcare_note, observation, healthcare_orders).
- **Patient portal** uses **frappe-ui** as its component library (`Card` and others) and its Tailwind preset (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The only theme extension is legacy colour aliases (lightBlue→sky, warmGray→stone, trueGray→neutral, coolGray→gray, blueGray→slate). Icons are feather-icons and lucide (`lucideIcons: true`).
- **Portal styling:** Tailwind utility classes directly in SFC templates, e.g. `text-2xl font-bold text-gray-900`, `text-sm text-gray-500`, `p-5 rounded-xl shadow-sm`, with accent `text-green-600` for amounts. Use the frappe-ui and Tailwind gray scale rather than custom hex values.
