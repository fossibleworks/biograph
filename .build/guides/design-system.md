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
---

- **Desk UI** (most of the app) uses the stock Frappe desk. That includes DocType forms defined in JSON, list, calendar, and tree views, workspaces (`workspace_sidebar/*.json`), number cards, and dashboard charts. Customizations go through `frappe.ui.form`, Frappe dialogs, and small Jinja HTML templates in `healthcare/public/js` (e.g. `healthcare_orders.html`, `observation.html`). Do not introduce a separate component library into desk scripts.
- **Patient Portal** uses **frappe-ui** as its component library (`Card`, `ErrorMessage`, `Button`, dialogs, `createResource`). Design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). Its only extensions are legacy colour aliases (lightBlue, warmGray, trueGray, coolGray, blueGray). The existing components use Tailwind utilities such as gray text scales, `rounded-xl`, and `shadow-sm`. Icons come from feather and lucide (`lucideIcons: true`).
- Brand images live in `healthcare/public/images` (`biograph-app-icon.svg`, `healthcare.svg`).
